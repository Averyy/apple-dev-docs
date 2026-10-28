# allowsParallelizedExport

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the session can parallelize its export operation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var allowsParallelizedExport: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsParallelizedExport;
```

## Discussion

This value is [`true`](../../Swift/true.md) by default, which indicates that the export session is allowed to expedite its processing by using additional resources in parallel on select Mac systems. If parallelization isn’t achievable, export proceeds as normal.

> **Note**:  Parallelized exports reduce the amount of time it takes to export media, but require additional power consumption. If your app requires opting out of the default behavior, set this value to [`false`](../../Swift/false.md).

## See Also

### Configuring output
- [var supportedFileTypes: [AVFileType]](./supportedfiletypes.md)
  An array containing the types of files the session can write.
- [var shouldOptimizeForNetworkUse: Bool](./shouldoptimizefornetworkuse.md)
  A Boolean value that indicates whether to optimize the movie for network use.
- [var canPerformMultiplePassesOverSourceMediaData: Bool](./canperformmultiplepassesoversourcemediadata.md)
  A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [var timeRange: CMTimeRange](./timerange.md)
  The time range of the source asset to export.
- [var fileLengthLimit: Int64](./filelengthlimit.md)
  The file length that the output of the session must not exceed.
- [var directoryForTemporaryFiles: URL?](./directoryfortemporaryfiles.md)
  A directory suitable to store temporary files that the export process generates.
- [outputURL](./outputurl.md)
  A URL where an asset export session writes its output.
- [outputFileType](./outputfiletype.md)
  The file type of the output an asset export session writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/allowsparallelizedexport)*