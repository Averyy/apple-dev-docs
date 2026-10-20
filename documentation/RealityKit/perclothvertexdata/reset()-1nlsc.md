# reset()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Resets the per-vertex data of each vertex to the default position constraint.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func reset()
```

Available when `ElementType` is `ClothBodyComponent.TargetShape.PositionConstraint`.

**Other overloads**:

```swift
mutating func reset()
```

```swift
mutating func reset()
```

## See Also

### Setting vertex values
- [func set(vertexIndices: [UInt32], value: ElementType)](./set%28vertexindices,value%29.md)
  Sets the data for the given vertex indices to a common value.
- [func setAll(value: ElementType)](./setall%28value%29.md)
  Sets the data for all vertices to a common value.
- [func reset()](./reset%28%29-403m8.md)
  Resets the per-vertex data of each vertex to a zero-force external force.
- [func reset()](./reset%28%29-4x5xi.md)
  Resets the per-vertex data of each vertex to the default motion type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perclothvertexdata/reset()-1nlsc)*