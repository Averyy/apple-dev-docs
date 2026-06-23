# setTexture(_:at:)

**Framework**: RealityKit  
**Kind**: method

Binds a Metal texture to a parameter at the given index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func setTexture(_ texture: (any MTLTexture)?, at index: Int)
```

## Parameters

- `texture`: The `MTLTexture` to bind, or `nil` to unbind the current texture.
- `index`: The index of the texture parameter in the texture table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/settexture(_:at:))*