# metadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The metadata an export session writes to the output container file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var metadata: [AVMetadataItem]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<AVMetadataItem *> * metadata;
```

## See Also

### Configuring metadata
- [var metadataItemFilter: AVMetadataItemFilter?](./metadataitemfilter.md)
  An object the export session uses to filter the metadata items it transfers to the output asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/metadata)*