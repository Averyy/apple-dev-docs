# set(vertexIndices:value:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Sets the data for the given vertex indices to a common value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func set(vertexIndices: [UInt32], value: ElementType)
```

## Parameters

- `vertexIndices`: The indices of the vertices to update.
- `value`: The value to assign to each of the specified vertices.

## See Also

### Setting vertex values
- [func setAll(value: ElementType)](./setall%28value%29.md)
  Sets the data for all vertices to a common value.
- [func reset()](./reset%28%29-1nlsc.md)
  Resets the per-vertex data of each vertex to the default position constraint.
- [func reset()](./reset%28%29-403m8.md)
  Resets the per-vertex data of each vertex to a zero-force external force.
- [func reset()](./reset%28%29-4x5xi.md)
  Resets the per-vertex data of each vertex to the default motion type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perclothvertexdata/set(vertexindices:value:))*