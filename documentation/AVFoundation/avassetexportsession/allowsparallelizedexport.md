# allowsParallelizedExport

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the session can parallelize its export operation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var allowsParallelizedExport: Bool { get set }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/swift/true) by default, which indicates that the export session is allowed to expedite its processing by using additional resources in parallel on select Mac systems. If parallelization isn’t achievable, export proceeds as normal.

> **Note**:  Parallelized exports reduce the amount of time it takes to export media, but require additional power consumption. If your app requires opting out of the default behavior, set this value to [`false`](https://developer.apple.com/documentation/swift/false).

 Parallelized exports reduce the amount of time it takes to export media, but require additional power consumption. If your app requires opting out of the default behavior, set this value to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var outputURL: URL?](avassetexportsession/outputurl.md)
  A URL where an asset export session writes its output.
- [var outputFileType: AVFileType?](avassetexportsession/outputfiletype.md)
  The file type of the output an asset export session writes.
- [var supportedFileTypes: [AVFileType]](avassetexportsession/supportedfiletypes.md)
  An array containing the types of files the session can write.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/allowsparallelizedexport)*