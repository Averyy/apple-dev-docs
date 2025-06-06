# directoryForTemporaryFiles

**Framework**: AVFoundation  
**Kind**: property

A directory to contain temporary files that the export process generates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var directoryForTemporaryFiles: URL? { get set }
```

#### Discussion

In some configurations, such as performing multipass encoding, an asset writer may need to write temporary files. Use this property value to set the file-system location where it writes temporary files. The system deletes all temporary files after it finishes writing successfully, fails, or you cancel the writing session.

You can set this value after writing starts.

## See Also

- [var metadata: [AVMetadataItem]](avassetwriter/metadata.md)
  An array of metadata items to write to the output file.
- [var shouldOptimizeForNetworkUse: Bool](avassetwriter/shouldoptimizefornetworkuse.md)
  A Boolean value that indicates whether to write the output file to make it more suitable for playback over a network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/directoryfortemporaryfiles)*