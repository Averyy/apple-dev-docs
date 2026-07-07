# setTexture(_:at:)

**Framework**: Compute Graph  
**Kind**: method

Binds a Metal texture to the texture slot at the given index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
final func setTexture(_ texture: (any MTLTexture)?, at index: Int)
```

## Parameters

- `texture`: The `MTLTexture` to bind, or `nil` to clear.
- `index`: The zero-based slot index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/settexture(_:at:))*