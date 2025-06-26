# init(texture:size:highlight:offset:colorTint:)

**Framework**: Touch Controller  
**Kind**: init

Creates a new sprite renderer with the specified texture, size, highlight texture, offset, and color tint.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(texture: any MTLTexture, size: CGSize, highlight highlightTexture: (any MTLTexture)?, offset: CGPoint, colorTint: CGColor)
```

#### Return Value

A new `TCSpriteRenderer` instance.

## Parameters

- `texture`: The Metal texture to use for the sprite.
- `size`: The size of the sprite in points.
- `highlightTexture`: The Metal texture to use for the sprite when highlighted. May be  .
- `offset`: The offset from the center of the parent control in points.
- `colorTint`: The color tint to apply to the texture. The color ref is retained.

## See Also

- [convenience init(texture: any MTLTexture, size: CGSize)](tcspriterenderer/init(texture:size:).md)
  Creates a new sprite renderer with the specified texture and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcspriterenderer/init(texture:size:highlight:offset:colortint:))*