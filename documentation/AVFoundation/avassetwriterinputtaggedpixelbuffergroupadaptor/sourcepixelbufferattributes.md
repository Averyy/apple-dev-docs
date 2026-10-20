# sourcePixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The attributes of buffers that the adaptor’s pixel buffer pool vends.

**Availability**:
- iOS 17.0+ - Deprecated in 27.0
- iPadOS 17.0+ - Deprecated in 27.0
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:) instead

## Declaration

```swift
var sourcePixelBufferAttributes: [String : any Sendable]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * sourcePixelBufferAttributes;
```

#### Discussion

The value of this property is a dictionary containing pixel buffer attribute keys defined in `<CoreVideo/CVPixelBuffer.h>`.

## See Also

### Configuring the buffer pool
- [var pixelBufferPool: CVPixelBufferPool?](./pixelbufferpool.md)
  A pixel buffer pool that vends and efficiently recycles the pixel buffers of tagged buffer groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/sourcepixelbufferattributes)*