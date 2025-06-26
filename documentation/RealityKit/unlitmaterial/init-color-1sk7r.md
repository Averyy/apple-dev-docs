# init(color:)

**Framework**: RealityKit  
**Kind**: init

Creates an unlit material with the given base color.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
init(color: NSColor)
```

#### Discussion

> **Note**: The blending mode of `UnlitMaterial` materials should be configured explicitly with the [`blending`](unlitmaterial/blending-swift.property.md) property for transparent or translucent surfaces.  The `opaque` mode is used when unset.

## Parameters

- `color`: The base color for the new material.

## See Also

- [init()](unlitmaterial/init.md)
  Creates an unlit material.
- [init(color: UIColor)](unlitmaterial/init(color:)-1h0ca.md)
  Creates an unlit material with the given base color.
- [init(applyPostProcessToneMap:)](unlitmaterial/init(applypostprocesstonemap:).md)
  Creates an UnlitMaterial with the given tone mapping setting
- [init(color: NSColor, applyPostProcessToneMap: Bool)](unlitmaterial/init(color:applypostprocesstonemap:)-2cszc.md)
  Creates an UnlitMaterial with the given color and tone mapping setting
- [init(color: UIColor, applyPostProcessToneMap: Bool)](unlitmaterial/init(color:applypostprocesstonemap:)-9pbcy.md)
  Creates an UnlitMaterial with the given color and tone mapping setting
- [init(program:)](unlitmaterial/init(program:).md)
- [init(texture:)](unlitmaterial/init(texture:).md)
  Creates a new unlit material with the provided color texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/init(color:)-1sk7r)*