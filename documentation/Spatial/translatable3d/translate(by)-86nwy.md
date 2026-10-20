# translate(by:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Translates the entity by the specified size.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Use `Vector3D` variant.

## Declaration

```swift
mutating func translate(by size: Size3D)
```

## Parameters

- `size`: The size structure that defines the translation.

## Default Implementations

### Translatable3D Implementations
- [func translate(by: Vector3D)](./translate%28by%29-3rlhd.md)
- [func translate(by: Size3D)](./translate%28by%29-6aq88.md)
  Translates the entity by the specified size.

## See Also

### Deprecated methods
- [func translated(by: Size3D) -> Self](./translated%28by%29-9ndur.md)
  Returns the entity that results from translating with the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/translatable3d/translate(by:)-86nwy)*