# commandBuffer

**Framework**: Metal  
**Kind**: property  
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

#### Discussion

This property may return undefined results if you call it after calling [`endEncoding()`](mtl4commandencoder/endencoding().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/commandbuffer)*