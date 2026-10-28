# init(color:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an unlit material with the given base color.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
init(color: UIColor)
```

**Other overloads**:

```swift
init(color: NSColor)
```

## Discussion

> **Note**: The blending mode of `UnlitMaterial` materials should be configured explicitly with the [`blending`](./blending-swift.property.md) property for transparent or translucent surfaces.  The `opaque` mode is used when unset.

## Parameters

- `color`: The base color for the new material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/init(color:)-5zgo5)*