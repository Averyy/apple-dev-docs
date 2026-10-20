# argumentBuffersSupport

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns the GPU device’s support tier for argument buffers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var argumentBuffersSupport: MTLArgumentBuffersTier { get }
```

```objc
@property (readonly) MTLArgumentBuffersTier argumentBuffersSupport;
```

## Mentions

- [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md)

## Topics

### Argument buffer tiers
- [enum MTLArgumentBuffersTier](../mtlargumentbufferstier.md)
  The values that determine the limits and capabilities of argument buffers.

## See Also

### Creating argument buffer encoders
- [var maxArgumentBufferSamplerCount: Int](./maxargumentbuffersamplercount.md)
  The maximum number of unique argument buffer samplers per app.
- [func makeArgumentEncoder(arguments: [MTLArgumentDescriptor]) -> (any MTLArgumentEncoder)?](./makeargumentencoder%28arguments%29.md)
  Creates a new argument encoder for an array of arguments.
- [func makeArgumentEncoder(bufferBinding: any MTLBufferBinding) -> any MTLArgumentEncoder](./makeargumentencoder%28bufferbinding%29.md)
  Creates a new argument encoder for a buffer binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/argumentbufferssupport)*