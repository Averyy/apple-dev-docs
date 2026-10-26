# supportedFileTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array containing the types of files the session can write.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var supportedFileTypes: [AVFileType] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * supportedFileTypes;
```

## See Also

### Configuring output
- [var allowsParallelizedExport: Bool](./allowsparallelizedexport.md)
  A Boolean value that indicates whether the session can parallelize its export operation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/supportedfiletypes)*