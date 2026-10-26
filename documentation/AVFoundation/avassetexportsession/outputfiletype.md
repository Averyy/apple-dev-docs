# outputFileType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The file type of the output an asset export session writes.

**Availability**:
- iOS 4.0+ - Deprecated in 27.0
- iPadOS 4.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use `export(to:as:)` instead.

## Declaration

```swift
var outputFileType: AVFileType? { get set }
```

```objc
@property (nonatomic, copy, nullable) AVFileType outputFileType;
```

## See Also

### Configuring output
- [outputURL](./outputurl.md)
  A URL where an asset export session writes its output.
- [supportedFileTypes](./supportedfiletypes.md)
  An array containing the types of files the session can write.
- [allowsParallelizedExport](./allowsparallelizedexport.md)
  A Boolean value that indicates whether the session can parallelize its export operation.
- [shouldOptimizeForNetworkUse](./shouldoptimizefornetworkuse.md)
  A Boolean value that indicates whether to optimize the movie for network use.
- [canPerformMultiplePassesOverSourceMediaData](./canperformmultiplepassesoversourcemediadata.md)
  A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [timeRange](./timerange.md)
  The time range of the source asset to export.
- [fileLengthLimit](./filelengthlimit.md)
  The file length that the output of the session must not exceed.
- [directoryForTemporaryFiles](./directoryfortemporaryfiles.md)
  A directory suitable to store temporary files that the export process generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/outputfiletype)*