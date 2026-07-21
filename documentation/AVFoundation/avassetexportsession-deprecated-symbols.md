# Deprecated symbols

**Framework**: AVFoundation

Review unsupported symbols and their replacements.

## Topics

### Accessing export presets
- [class func exportPresets(compatibleWith: AVAsset) -> [String]](avassetexportsession/exportpresets(compatiblewith:).md)
  Returns compatible export presets for the asset.
### Configuring output
- [var outputURL: URL?](avassetexportsession/outputurl.md)
  A URL where an asset export session writes its output.
- [var outputFileType: AVFileType?](avassetexportsession/outputfiletype.md)
  The file type of the output an asset export session writes.
### Exporting media
- [func exportAsynchronously(completionHandler: () -> Void)](avassetexportsession/exportasynchronously(completionhandler:).md)
  Starts the asynchronous execution of an export session.
- [func cancelExport()](avassetexportsession/cancelexport.md)
  Cancels the execution of an export session.
### Monitoring export progress
- [var status: AVAssetExportSession.Status](avassetexportsession/status-swift.property.md)
  The status of the export session.
- [var progress: Float](avassetexportsession/progress.md)
  A value that indicates the progress of the export.
- [var error: (any Error)?](avassetexportsession/error.md)
  An optional error object.
### Estimating file length and duration
- [var estimatedOutputFileLength: Int64](avassetexportsession/estimatedoutputfilelength.md)
  The estimated length of the exported file, in bytes.
### Estimating duration
- [var maxDuration: CMTime](avassetexportsession/maxduration.md)
  Provides an estimate of the maximum duration of the exported media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession-deprecated-symbols)*