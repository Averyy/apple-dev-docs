# Adding a display mask rectangle metadata track to a movie file

**Framework**: AVFoundation

Show a specific area of a video by using timed display mask rectangle metadata.

**Availability**:
- macOS 26.0+
- Xcode 26.0+

#### Overview

A QuickTime movie can provide display mask rectangle metadata that indicates the area of a video to show during playback. On visionOS 26 and later, the system reads this metadata and crops the video to the specified display area and renders the area outside the display mask as transparent. You can use a display mask to remove the encoded black letterbox or pillarbox at rendering time, or dynamically change the visible portion of a video for creative effects.

This sample is a command-line app that demonstrates how to create a QuickTime movie file with display mask rectangle metadata. It adds a timed metadata track to store the display mask rectangle metadata, and associates a render track reference to the video to signal the association to the video playback system.

The screen recordings below show how the display mask rectangle metadata (two types) added by the sample app affects displayed video compared to the original movie file.

> **Note**: For information on the details of this metadata type, see [`Rectangular Mask Payload Metadata within the QuickTime Movie File Format - Format addition`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Rectangular-Dynamic-Mask-Metadata.pdf).

#### Configure the Sample Code Project

The sample requires three arguments:

```bash
./AVAddDisplayMaskTrack <input-path> <output-path> <display-mask-type>
```

- **`<input-path>`**: The path to the existing source QuickTime movie file with a video track.
- **`<output-path>`**: The path to the new output QuickTime movie file, which includes the source movie file’s media tracks with the additional display mask rectangle timed metadata track.
- **`<display-mask-type>`**: An integer type for the display mask. There are only two types, `1` or `2`; the default is `1` if the third argument isn’t provided or not a valid value.

The `display-mask-type` argument indicates the display mask to write to the movie file:

- Type 1 display mask is a static square that’s 75 percent of the shorter side of the video’s dimensions, and centered on the video frame for the entire duration of the movie. For example, if the video’s dimensions are 1920 x 1080, then the display mask is 810 x 810 (1080 `*` 0.75 = 810), and centered at (960, 540).
- Type 2 display mask is a per-frame square mask that’s 30 percent of the shorter side of the video’s dimensions, and moves across the video frame. This type illustrates dynamic display mask metadata that updates at the associated video track’s frame rate.

#### Set Up a Display Mask Rectangle Metadata Track

The sample provides a `MovieProcessor` class that contains the app’s metadata processing logic. When you run the app, it passes the command-line arguments you specify to the `MovieProcessor` class’s `processMovie(inputPath:outputPath:displayMaskType:)` method. This method sets up the reading and writing functionality using [`AVAssetReader`](avassetreader.md) and [`AVAssetWriter`](avassetwriter.md), respectively.

To allow the app to append metadata during asset writing, this method calls `addDisplayMaskMetadataTrack(to:videoInput:videoInfo:)` to create an [`AVAssetWriterInput`](avassetwriterinput.md) that writes a timed metadata track for the display mask rectangle. Before creating the writer input, this method creates a [`CMMetadataFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMMetadataFormatDescription) for the display mask metadata. The format description uses the boxed metadata (`mebx`) type and pairs the [`kCMMetadataIdentifier_QuickTimeMetadataDisplayMaskRectangleMono`](https://developer.apple.com/documentation/CoreMedia/kCMMetadataIdentifier_QuickTimeMetadataDisplayMaskRectangleMono) identifier with the [`kCMMetadataBaseDataType_RasterRectangleValue`](https://developer.apple.com/documentation/CoreMedia/kCMMetadataBaseDataType_RasterRectangleValue) data type:

```swift
// Define the metadata specifications for the monoscopic display mask rectangle.
let metadataSpecifications: [[String: Any]] = [[
    kCMMetadataFormatDescriptionMetadataSpecificationKey_Identifier as String:
        kCMMetadataIdentifier_QuickTimeMetadataDisplayMaskRectangleMono as String,
    kCMMetadataFormatDescriptionMetadataSpecificationKey_DataType as String:
        kCMMetadataBaseDataType_RasterRectangleValue as String
]]

// Create the `CMMetadataFormatDescription` for the monoscopic display mask rectangle
// in boxed metadata (`mebx`) type.
var metadataFormatDesc: CMMetadataFormatDescription? = nil
let status = CMMetadataFormatDescriptionCreateWithMetadataSpecifications(
    allocator: kCFAllocatorDefault,
    metadataType: kCMMetadataFormatType_Boxed,
    metadataSpecifications: metadataSpecifications as CFArray,
    formatDescriptionOut: &metadataFormatDesc
)
```

> **Note**: The `metadataSpecifications` array can contain additional identifier and data type pairs if you need to store other metadata within this timed metadata track. For list of additional metadata identifiers and data types, see [`CMMetadata`](https://developer.apple.com/documentation/CoreMedia/cmmetadata).

With the format description in place, the method creates an [`AVAssetWriterInput`](avassetwriterinput.md) for the metadata track. It sets [`expectsMediaDataInRealTime`](avassetwriterinput/expectsmediadatainrealtime.md) to `false` because the app writes metadata samples as fast as it can process them, rather than receiving them from a live capture source. It also sets the [`mediaTimeScale`](avassetwriterinput/mediatimescale.md) to match the video track to align the metadata sample timestamps precisely with the video frames:

```swift
// Create the `AVAssetWriterInput` for the display mask metadata track and attach it to `AVAssetWriter`.
metadataInput = AVAssetWriterInput(mediaType: .metadata, outputSettings: nil, sourceFormatHint: metadataFormatDesc)
guard let metadataInput else {
    throw ProcessingError.writerInputCreationFailed("DisplayMask metadata.")
}

metadataInput.expectsMediaDataInRealTime = false
metadataInput.mediaTimeScale = videoInfo.timescale
```

The method then creates an [`AVAssetWriterInputMetadataAdaptor`](avassetwriterinputmetadataadaptor.md) to append timed metadata groups to the writer input. The adaptor provides a convenient way to write [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) objects, which package metadata items with their time ranges, rather than working directly with sample buffers:

```swift
// Create the metadata adaptor for the display mask metadata's `AVAssetWriterInput`.
metadataAdaptor = AVAssetWriterInputMetadataAdaptor(assetWriterInput: metadataInput)
```

Finally, the method adds the metadata input to the asset writer and establishes a track association between the metadata track and the video track. The render metadata source association (`rndr`) is required so the playback system knows which video track the display mask metadata applies to. The playback system ignores this metadata when this association doesn’t exist.

```swift
if writer.canAdd(metadataInput) {
    writer.add(metadataInput)

    // Add the `rndr` track association between the display mask metadata track and
    // the enabled video track.
    metadataInput.addTrackAssociation(withTrackOf: videoInput, type: AVAssetTrack.AssociationType.renderMetadataSource.rawValue)
} else {
    throw ProcessingError.cannotAddWriterInput("DisplayMask metadata.")
}
```

#### Write Display Mask Rectangle Metadata

The `setupDisplayMaskMetadataTransfer(videoInfo:maskType:)` method handles writing the display mask metadata samples to the timed metadata track. This method uses the video track’s dimensions to calculate the raster rectangle parameters and writes the metadata samples using the adaptor created earlier.

Depending on the display mask type you specify at the command line, the method takes one of two paths:

- Type 1 creates a static display mask —– a single centered square that remains fixed for the video’s duration.
- Type 2 creates a dynamic display mask —– a smaller square that moves across the frame, with a new metadata sample for each video frame.

To see the specific calculations each path uses, see `MovieProcessor.swift` file in the sample project and look at `Type 1 static display mask calculation.` and `Type 2 dynamic display mask initialization/update calculation.` marks.

Despite writing different metadata, both paths follow a similar pattern. They request data from the metadata input when it’s ready, create a timed metadata group for the display mask rectangle, and append it to the metadata adaptor:

```swift
metadataInput.requestMediaDataWhenReady(on: queue) {
    while metadataInput.isReadyForMoreMediaData {
        let rasterRectangle = // Calculate the raster rectangle parameters for this media sample.

        // Create the timed metadata group and append it.
        let metadataGroup = self.createMetadataGroupForDisplayMask(
            rasterRectangle: rasterRectangle,
            sampleTime: sampleTime,
            sampleDuration: sampleDuration
        )
        // Append the metadata group.
        metadataAdaptor.append(metadataGroup)
    }
}
```

The `createMetadataGroupForDisplayMask(rasterRectangle:sampleTime:sampleDuration:)` method creates the timed metadata group:

```swift
private func createMetadataGroupForDisplayMask(rasterRectangle: [Int],
                sampleTime: CMTime, sampleDuration: CMTime) -> AVTimedMetadataGroup {
    let metadataItem = AVMutableMetadataItem()
    metadataItem.identifier = AVMetadataIdentifier(
        kCMMetadataIdentifier_QuickTimeMetadataDisplayMaskRectangleMono as String)
    metadataItem.value = rasterRectangle as NSArray
    metadataItem.dataType = kCMMetadataBaseDataType_RasterRectangleValue as String

    // Wrap the metadata item in `AVTimedMetadataGroup`.
    let timedMetadataGroup = AVTimedMetadataGroup(
        items: [metadataItem],
        timeRange: CMTimeRange(start: sampleTime, duration: sampleDuration)
    )

    return timedMetadataGroup
}
```

This method creates an [`AVMutableMetadataItem`](avmutablemetadataitem.md) with the display mask identifier and data type, sets its value to the raster rectangle array, and wraps it in an [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) with the specified time range. The `rasterRectangle` parameter is an array of six integers: `[rasterWidth, rasterHeight, left, width, top, height]`. The time range determines when this metadata applies during playback:

- For a static mask, time range spans the entire video duration.
- For a dynamic mask, time range matches the duration of a single video frame.

When the asset writer finishes, the output file contains the original video with the display mask rectangle metadata track. On visionOS 26 or later, you can play the file in apps like Files to see the display mask effect.

## See Also

- [Converting projected video to Apple Projected Media Profile](converting-projected-video-to-apple-projected-media-profile.md)
  Convert content with equirectangular or half-equirectangular projection to APMP.
- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md)
  Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Writing fragmented MPEG-4 files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md)
  Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
- [Creating spatial photos and videos with spatial metadata](../ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata.md)
  Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging media with video color information](tagging-media-with-video-color-information.md)
  Inspect and set video color space information when writing and transcoding media.
- [Evaluating an app’s video color](evaluating-an-app-s-video-color.md)
  Check color reproduction for a video in your app by using test patterns, video test equipment, and light-measurement instruments.
- [class AVOutputSettingsAssistant](avoutputsettingsassistant.md)
  An object that builds audio and video output settings dictionaries.
- [class AVAssetWriter](avassetwriter.md)
  An object that writes media data to a container file.
- [class AVAssetWriterInput](avassetwriterinput.md)
  An object that appends media samples to a track in an asset writer’s output file.
- [class AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md)
  An object that appends video samples to an asset writer input.
- [class AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md)
  An object that appends tagged buffer groups to an asset writer input.
- [class AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md)
  An object that appends timed metadata groups to an asset writer input.
- [class AVAssetWriterInputGroup](avassetwriterinputgroup.md)
  A group of inputs with tracks that are mutually exclusive to each other for playback or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/adding-a-display-mask-rectangle-metadata-track-to-a-movie-file)*