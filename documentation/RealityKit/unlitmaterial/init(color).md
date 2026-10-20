# init(color:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an unlit material with the given base color.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(color: NSColor)
```

**Other overloads**:

```swift
init(color: UIColor)
```

#### Discussion

> **Note**: The blending mode of `UnlitMaterial` materials should be configured explicitly with the [`blending`](./blending-swift.property.md) property for transparent or translucent surfaces.  The `opaque` mode is used when unset.

## Parameters

- `color`: The base color for the new material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/init(color:))*