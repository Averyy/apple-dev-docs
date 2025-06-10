# init(tint:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a sheen color in macOS.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
init(tint: UIColor = .white, texture: MaterialParameters.Texture? = nil)
```

#### Discussion

This initializer creates an object from a color, an image texture, or from both. If you don’t provide a `tint` color, `tint` defaults to white.

If you specify `texture`, RealityKit calculates the final sheen color for the entity by UV-mapping `texture` onto the entity and then multiplying the color at any given pixel by `tint`. If `tint` is white, RealityKit uses the texture untinted.

If you don’t specify `texture`, then RealityKit uses `tint` as the entity’s sheen color.

## Parameters

- `tint`: The tint color.
- `texture`: The optional image texture.

## See Also

- [init(tint: NSColor, texture: MaterialParameters.Texture?)](physicallybasedmaterial/sheencolor/init(tint:texture:)-12ev9.md)
  Creates a sheen color in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/sheencolor/init(tint:texture:)-6kcl7)*