# metadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of metadata items to write to the output file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var metadata: [AVMetadataItem] { get set }
```

```objc
@property (nonatomic, copy) NSArray<AVMetadataItem *> * metadata;
```

## Discussion

You can’t modify this property value after writing starts.

## See Also

### Configuring output
- [var shouldOptimizeForNetworkUse: Bool](./shouldoptimizefornetworkuse.md)
  A Boolean value that indicates whether to write the output file to make it more suitable for playback over a network.
- [var directoryForTemporaryFiles: URL?](./directoryfortemporaryfiles.md)
  A directory to contain temporary files that the export process generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/metadata)*