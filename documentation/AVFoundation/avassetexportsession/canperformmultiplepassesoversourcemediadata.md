# canPerformMultiplePassesOverSourceMediaData

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var canPerformMultiplePassesOverSourceMediaData: Bool { get set }
```

#### Discussion

When the value for this property is [`true`](https://developer.apple.com/documentation/swift/true), the export session can produce higher quality results at the expense of longer export times. Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) may also require the export session to write temporary data to disk during the export. To control the location of temporary data, use the property [`directoryForTemporaryFiles`](avassetexportsession/directoryfortemporaryfiles.md).

The default value is [`false`](https://developer.apple.com/documentation/swift/false). Not all export session configurations can benefit from performing multiple passes over the source media. In these cases, setting this property to [`true`](https://developer.apple.com/documentation/swift/true) has no effect.

You can’t set this property after the export starts.

## See Also

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
- [var timeRange: CMTimeRange](avassetexportsession/timerange.md)
  The time range of the source asset to export.
- [var fileLengthLimit: Int64](avassetexportsession/filelengthlimit.md)
  The file length that the output of the session must not exceed.
- [var directoryForTemporaryFiles: URL?](avassetexportsession/directoryfortemporaryfiles.md)
  A directory suitable to store temporary files that the export process generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/canperformmultiplepassesoversourcemediadata)*