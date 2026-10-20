# canPerformMultiplePassesOverSourceMediaData

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL canPerformMultiplePassesOverSourceMediaData;
```

#### Discussion

When the value for this property is [`true`](../../Swift/true.md), the export session can produce higher quality results at the expense of longer export times. Setting this property to [`true`](../../Swift/true.md) may also require the export session to write temporary data to disk during the export. To control the location of temporary data, use the property [`directoryForTemporaryFiles`](./directoryfortemporaryfiles.md).

The default value is [`false`](../../Swift/false.md). Not all export session configurations can benefit from performing multiple passes over the source media. In these cases, setting this property to [`true`](../../Swift/true.md) has no effect.

You can’t set this property after the export starts.

## See Also

### Configuring output
- [var supportedFileTypes: [AVFileType]](./supportedfiletypes.md)
  An array containing the types of files the session can write.
- [var allowsParallelizedExport: Bool](./allowsparallelizedexport.md)
  A Boolean value that indicates whether the session can parallelize its export operation.
- [var shouldOptimizeForNetworkUse: Bool](./shouldoptimizefornetworkuse.md)
  A Boolean value that indicates whether to optimize the movie for network use.
- [var timeRange: CMTimeRange](./timerange.md)
  The time range of the source asset to export.
- [var fileLengthLimit: Int64](./filelengthlimit.md)
  The file length that the output of the session must not exceed.
- [var directoryForTemporaryFiles: URL?](./directoryfortemporaryfiles.md)
  A directory suitable to store temporary files that the export process generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/canperformmultiplepassesoversourcemediadata)*