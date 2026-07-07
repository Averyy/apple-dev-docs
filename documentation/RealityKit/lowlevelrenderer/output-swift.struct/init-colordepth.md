# init(color:depth:)

**Framework**: RealityKit  
**Kind**: init

Creates an output configuration with the given color and depth texture targets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(color: LowLevelRenderer.Output.Texture? = nil, depth: LowLevelRenderer.Output.Texture? = nil)
```

## Parameters

- `color`: The color output texture, or `nil` for depth-only passes. Defaults to `nil`.
- `depth`: The depth output texture, or `nil` to omit depth. Defaults to `nil`.

## See Also

- [LowLevelRenderer.Output.Texture](lowlevelrenderer/output-swift.struct/texture.md)
  A reference to a specific mip level, slice, and depth plane within a Metal texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/init(color:depth:))*