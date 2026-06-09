# init(color:)

**Framework**: RealityKit  
**Kind**: init

Creates an unlit material with the given base color.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(color: NSColor)
```

#### Discussion

> **Note**: The blending mode of `UnlitMaterial` materials should be configured explicitly with the [`blending`](unlitmaterial/blending-swift.property.md) property for transparent or translucent surfaces.  The `opaque` mode is used when unset.

## Parameters

- `color`: The base color for the new material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/init(color:))*