# setScissorRects(_:)

**Framework**: Metal  
**Kind**: method

Sets an array of scissor rectangles for a fragment scissor test.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setScissorRects(_ scissorRects: [MTLScissorRect])
```

#### Discussion

Metal uses the specific scissor rectangle corresponding to the index you specify via the `[[ viewport_array_index ]]` output attribute of the vertex shader function in the Metal Shading Language, discarding all fragments outside of the scissor rect.

## Parameters

- `scissorRects`: A Swift array of   elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setscissorrects(_:))*