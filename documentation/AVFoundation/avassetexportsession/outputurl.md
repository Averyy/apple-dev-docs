# outputURL

**Framework**: AVFoundation  
**Kind**: property

A URL where an asset export session writes its output.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var outputURL: URL? { get set }
```

#### Discussion

This property value is key-value observable.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/outputurl)*