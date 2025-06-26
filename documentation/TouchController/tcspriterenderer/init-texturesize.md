# init(texture:size:)

**Framework**: Touch Controller  
**Kind**: init

Creates a new sprite renderer with the specified texture and size.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(texture: any MTLTexture, size: CGSize)
```

#### Return Value

A new `TCSpriteRenderer` instance.

## Parameters

- `texture`: The Metal texture to use for the sprite.
- `size`: The size of the sprite in points.

## See Also

- [init(texture: any MTLTexture, size: CGSize, highlight: (any MTLTexture)?, offset: CGPoint, colorTint: CGColor)](tcspriterenderer/init(texture:size:highlight:offset:colortint:).md)
  Creates a new sprite renderer with the specified texture, size, highlight texture, offset, and color tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcspriterenderer/init(texture:size:))*