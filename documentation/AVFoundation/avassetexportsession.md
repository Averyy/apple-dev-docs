# AVAssetExportSession

**Framework**: AVFoundation  
**Kind**: class

An object that exports assets in a format that you specify using an export preset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetExportSession
```

## Mentions

- [Exporting video to alternative formats](exporting-video-to-alternative-formats.md)

#### Overview

You configure this object to export an instance of [`AVAsset`](avasset.md) by setting an export preset, an output file type, and an output URL.

## Topics

### Creating an export session
- [init?(asset: AVAsset, presetName: String)](avassetexportsession/init(asset:presetname:).md)
  Creates an export session with a preset configuration.
- [Export presets](export-presets.md)
  Configure an export session to output media in standard sizes and formats.
### Accessing export presets
- [var presetName: String](avassetexportsession/presetname.md)
  The name of the preset that the asset export session uses.
- [func determineCompatibleFileTypes(completionHandler: ([AVFileType]) -> Void)](avassetexportsession/determinecompatiblefiletypes(completionhandler:).md)
  Determines the output file types an asset export session supports writing in its current configuration.
- [class func allExportPresets() -> [String]](avassetexportsession/allexportpresets.md)
  Returns all available export preset names.
- [class func determineCompatibility(ofExportPreset: String, with: AVAsset, outputFileType: AVFileType?, completionHandler: (Bool) -> Void)](avassetexportsession/determinecompatibility(ofexportpreset:with:outputfiletype:completionhandler:).md)
  Determines an export preset’s compatibility to export the asset in a container of the output file type.
- [class func exportPresets(compatibleWith: AVAsset) -> [String]](avassetexportsession/exportpresets(compatiblewith:).md)
  Returns compatible export presets for the asset.
### Configuring output
- [var outputURL: URL?](avassetexportsession/outputurl.md)
  A URL where an asset export session writes its output.
- [var outputFileType: AVFileType?](avassetexportsession/outputfiletype.md)
  The file type of the output an asset export session writes.
- [var supportedFileTypes: [AVFileType]](avassetexportsession/supportedfiletypes.md)
  An array containing the types of files the session can write.
- [var allowsParallelizedExport: Bool](avassetexportsession/allowsparallelizedexport.md)
  A Boolean value that indicates whether the session can parallelize its export operation.
- [var shouldOptimizeForNetworkUse: Bool](avassetexportsession/shouldoptimizefornetworkuse.md)
  A Boolean value that indicates whether to optimize the movie for network use.
- [var canPerformMultiplePassesOverSourceMediaData: Bool](avassetexportsession/canperformmultiplepassesoversourcemediadata.md)
  A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [var timeRange: CMTimeRange](avassetexportsession/timerange.md)
  The time range of the source asset to export.
- [var fileLengthLimit: Int64](avassetexportsession/filelengthlimit.md)
  The file length that the output of the session must not exceed.
- [var directoryForTemporaryFiles: URL?](avassetexportsession/directoryfortemporaryfiles.md)
  A directory suitable to store temporary files that the export process generates.
### Configuring metadata
- [var metadata: [AVMetadataItem]?](avassetexportsession/metadata.md)
  The metadata an export session writes to the output container file.
- [var metadataItemFilter: AVMetadataItemFilter?](avassetexportsession/metadataitemfilter.md)
  An object the export session uses to filter the metadata items it transfers to the output asset.
### Configuring video output
- [var videoComposition: AVVideoComposition?](avassetexportsession/videocomposition.md)
  An optional object that provides instructions for how to composite frames of video.
- [var customVideoCompositor: (any AVVideoCompositing)?](avassetexportsession/customvideocompositor.md)
  An optional custom object to use when compositing video frames.
### Configuring track groups
- [var audioTrackGroupHandling: AVAssetTrackGroupOutputHandling](avassetexportsession/audiotrackgrouphandling.md)
  A policy that defines how the session exports alternate audio tracks.
- [struct AVAssetTrackGroupOutputHandling](avassettrackgroupoutputhandling.md)
  A type that specifies policies for how an export session processes alternate tracks in a track group.
### Configuring audio output
- [var audioMix: AVAudioMix?](avassetexportsession/audiomix.md)
  The parameters for audio mixing and an indication of whether to enable nondefault audio mixing for export.
- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](avassetexportsession/audiotimepitchalgorithm.md)
  A processing algorithm for managing audio pitch for scaled audio edits.
### Exporting media
- [func export(to: URL, as: AVFileType, isolation: isolated (any Actor)?) async throws](avassetexportsession/export(to:as:isolation:).md)
  Exports the asset to the output location in the specified file type.
- [func cancelExport()](avassetexportsession/cancelexport.md)
  Cancels the execution of an export session.
- [func exportAsynchronously(completionHandler: () -> Void)](avassetexportsession/exportasynchronously(completionhandler:).md)
  Starts the asynchronous execution of an export session.
### Monitoring export progress
- [func states(updateInterval: TimeInterval) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>
](avassetexportsession/states(updateinterval:).md)
  Monitors the progress state of an export operation.
- [AVAssetExportSession.State](avassetexportsession/state.md)
  Constants that indicate the state of an export operation.
- [var status: AVAssetExportSession.Status](avassetexportsession/status-swift.property.md)
  The status of the export session.
- [AVAssetExportSession.Status](avassetexportsession/status-swift.enum.md)
  Values that indicate the state of an export session.
- [var progress: Float](avassetexportsession/progress.md)
  A value that indicates the progress of the export.
- [var error: (any Error)?](avassetexportsession/error.md)
  An optional error object.
### Estimating file length and duration
- [func estimateOutputFileLength(completionHandler: (Int64, (any Error)?) -> Void)](avassetexportsession/estimateoutputfilelength(completionhandler:).md)
  Starts estimating the output file length of the export while considering the asset, preset, and time range configuration of the export session.
- [var estimatedOutputFileLength: Int64](avassetexportsession/estimatedoutputfilelength.md)
  The estimated length of the exported file, in bytes.
### Estimating duration
- [func estimateMaximumDuration(completionHandler: (CMTime, (any Error)?) -> Void)](avassetexportsession/estimatemaximumduration(completionhandler:).md)
  Starts estimating the maximum duration of the export while considering the asset, preset, and time range configuration of the export session.
- [var maxDuration: CMTime](avassetexportsession/maxduration.md)
  Provides an estimate of the maximum duration of the exported media.
### Accessing the asset
- [var asset: AVAsset](avassetexportsession/asset.md)
  An asset that a session exports.

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

- [Exporting video to alternative formats](exporting-video-to-alternative-formats.md)
  Convert an existing movie file to a different format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession)*