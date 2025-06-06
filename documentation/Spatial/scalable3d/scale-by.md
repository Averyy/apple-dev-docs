# scale(by:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

Scales the entity by the specified size.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
mutating func scale(by size: Size3D)
```

## Parameters

- `size`: The size structure that defines the scale.

## See Also

- [func scaleBy(x: Double, y: Double, z: Double)](scalable3d/scaleby(x:y:z:).md)
  Scales the entity by the specified values.
- [func scaled(by: Size3D) -> Self](scalable3d/scaled(by:).md)
  Returns the entity that results from scaling with the specified size.
- [func scaledBy(x: Double, y: Double, z: Double) -> Self](scalable3d/scaledby(x:y:z:).md)
  Returns the entity that results from scaling with the specified values.
- [func uniformlyScale(by: Double)](scalable3d/uniformlyscale(by:).md)
  Uniformly scales the entity by the specified scalar value.
- [func uniformlyScaled(by: Double) -> Self](scalable3d/uniformlyscaled(by:).md)
  Returns the entity that results from uniformly scaling with the specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scalable3d/scale(by:))*