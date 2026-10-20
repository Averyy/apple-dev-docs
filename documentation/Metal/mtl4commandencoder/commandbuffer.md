# commandBuffer

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns the command buffer that is currently encoding commands.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var commandBuffer: (any MTL4CommandBuffer)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<MTL4CommandBuffer> commandBuffer;
```

#### Discussion

This property may return undefined results if you call it after calling [`endEncoding()`](./endencoding%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/commandbuffer)*