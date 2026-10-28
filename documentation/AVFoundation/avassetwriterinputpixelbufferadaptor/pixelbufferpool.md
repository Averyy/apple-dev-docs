# pixelBufferPool

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A pool of pixel buffers to append to the adaptor’s input.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputPixelBufferReceiver(for:pixelBufferAttributes:) instead

## Declaration

```swift
var pixelBufferPool: CVPixelBufferPool? { get }
```

```objc
@property (nonatomic, readonly, nullable) CVPixelBufferPoolRef pixelBufferPool;
```

## Discussion

For maximum efficiency, you should create [CVPixelBuffer](../../CoreVideo/cvpixelbuffer-q2e.md) objects for [`append(_:withPresentationTime:)`](./append%28_,withpresentationtime%29.md) by using this pool with the [`CVPixelBufferPoolCreatePixelBuffer(_:_:_:)`](../../CoreVideo/cvpixelbufferpoolcreatepixelbuffer%28_,_,_%29.md) function.

This value is `nil` prior to calling [`startSession(atSourceTime:)`](../avassetwriter/startsession%28atsourcetime%29.md)on the associated [`AVAssetWriter`](../avassetwriter.md) object.

This property is key-value observable.

## See Also

### Accessing the pool
- [var sourcePixelBufferAttributes: [String : any Sendable]?](./sourcepixelbufferattributes.md)
  The attributes of the pixel buffers that the pool contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/pixelbufferpool)*