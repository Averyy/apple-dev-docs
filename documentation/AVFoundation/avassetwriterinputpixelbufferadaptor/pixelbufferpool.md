# pixelBufferPool

**Framework**: AVFoundation  
**Kind**: property

A pool of pixel buffers to append to the adaptor’s input.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var pixelBufferPool: CVPixelBufferPool? { get }
```

#### Discussion

For maximum efficiency, you should create [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) objects for [`append(_:withPresentationTime:)`](avassetwriterinputpixelbufferadaptor/append(_:withpresentationtime:).md) by using this pool with the [`CVPixelBufferPoolCreatePixelBuffer(_:_:_:)`](https://developer.apple.com/documentation/CoreVideo/CVPixelBufferPoolCreatePixelBuffer(_:_:_:)) function.

This value is `nil` prior to calling [`startSession(atSourceTime:)`](avassetwriter/startsession(atsourcetime:).md)on the associated [`AVAssetWriter`](avassetwriter.md) object.

This property is key-value observable.

## See Also

- [var sourcePixelBufferAttributes: [String : Any]?](avassetwriterinputpixelbufferadaptor/sourcepixelbufferattributes.md)
  The attributes of the pixel buffers that the pool contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/pixelbufferpool)*