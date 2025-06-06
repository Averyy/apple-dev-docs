# AVAssetReader

**Framework**: AVFoundation  
**Kind**: class

An object that reads media data from an asset.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetReader
```

#### Overview

Use an asset reader to read media data from instances of [`AVAsset`](avasset.md). The assets you read may represent file-based media like QuickTime movies or MPEG-4 files, or media that you compose from multiple sources using [`AVComposition`](avcomposition.md).

## Topics

### Creating an Asset Reader
- [init(asset: AVAsset) throws](avassetreader/init(asset:).md)
  Creates an object to read media data from an asset.
### Managing Outputs
- [func canAdd(AVAssetReaderOutput) -> Bool](avassetreader/canadd(_:).md)
  Determines whether you can add the output to the asset reader.
- [func add(AVAssetReaderOutput)](avassetreader/add(_:).md)
  Adds an output to the reader.
- [var outputs: [AVAssetReaderOutput]](avassetreader/outputs.md)
  The outputs from which you read media data.
### Configuring Reading
- [var timeRange: CMTimeRange](avassetreader/timerange.md)
  The time range within the asset to read.
- [var status: AVAssetReader.Status](avassetreader/status-swift.property.md)
  The status of reading sample buffers from the asset.
- [AVAssetReader.Status](avassetreader/status-swift.enum.md)
  Values that represent the possible states of an asset reader.
- [var error: (any Error)?](avassetreader/error.md)
  An error that describes the reason for a failure.
### Controlling Reading
- [func startReading() -> Bool](avassetreader/startreading.md)
  Prepares the asset reader to start reading sample buffers from the asset.
- [func cancelReading()](avassetreader/cancelreading.md)
  Cancels any background work and stops the reader’s outputs from reading more samples.
### Inspecting the Asset
- [var asset: AVAsset](avassetreader/asset.md)
  The asset from which to read media data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md)
  Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [class AVAssetReaderOutput](avassetreaderoutput.md)
  An abstract class that defines the interface to read media samples from an asset reader.
- [class AVAssetReaderTrackOutput](avassetreadertrackoutput.md)
  An object that reads media data from a single track of an asset.
- [class AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md)
  An object that reads audio samples that result from mixing audio from one or more tracks.
- [class AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md)
  An object that reads composited video frames from one or more tracks of an asset.
- [class AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md)
  An object that reads sample references from an asset track.
- [class AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md)
  An object that creates timed metadata group objects for an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader)*