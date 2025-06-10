# commandBuffer

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

Returns the command buffer that is currently encoding commands.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var commandBuffer: (any MTL4CommandBuffer)? { get }
```

#### Discussion

This property may return undefined results if you call it after calling [`endEncoding()`](mtl4commandencoder/endencoding().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/commandbuffer)*