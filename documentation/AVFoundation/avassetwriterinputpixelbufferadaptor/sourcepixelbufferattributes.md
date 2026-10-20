# sourcePixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The attributes of the pixel buffers that the pool contains.

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
var sourcePixelBufferAttributes: [String : any Sendable]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * sourcePixelBufferAttributes;
```

## See Also

### Accessing the pool
- [var pixelBufferPool: CVPixelBufferPool?](./pixelbufferpool.md)
  A pool of pixel buffers to append to the adaptor’s input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/sourcepixelbufferattributes)*