# metadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The metadata for the output file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var metadata: [AVMetadataItem]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<AVMetadataItem *> * metadata;
```

## Discussion

This array contains [`AVMetadataItem`](../avmetadataitem.md) objects. You use it to add metadata, such as copyright, creation date, and so on, to the recorded movie file.

## See Also

### Configuring movies
- [var movieFragmentInterval: CMTime](./moviefragmentinterval.md)
  The number of seconds of output that are written per fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/metadata)*