# fileLengthLimit

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The file length that the output of the session must not exceed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fileLengthLimit: Int64 { get set }
```

```objc
@property (nonatomic) long long fileLengthLimit;
```

## See Also

### Configuring output
- [var supportedFileTypes: [AVFileType]](./supportedfiletypes.md)
  An array containing the types of files the session can write.
- [var allowsParallelizedExport: Bool](./allowsparallelizedexport.md)
  A Boolean value that indicates whether the session can parallelize its export operation.
- [var shouldOptimizeForNetworkUse: Bool](./shouldoptimizefornetworkuse.md)
  A Boolean value that indicates whether to optimize the movie for network use.
- [var canPerformMultiplePassesOverSourceMediaData: Bool](./canperformmultiplepassesoversourcemediadata.md)
  A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [var timeRange: CMTimeRange](./timerange.md)
  The time range of the source asset to export.
- [var directoryForTemporaryFiles: URL?](./directoryfortemporaryfiles.md)
  A directory suitable to store temporary files that the export process generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/filelengthlimit)*