# set(vertexIndices:value:)

**Framework**: RealityKit  
**Kind**: method

Sets the data for the given vertex indices to a common value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func set(vertexIndices: [UInt32], value: ElementType)
```

## Parameters

- `vertexIndices`: The indices of the vertices to update.
- `value`: The value to assign to each of the specified vertices.

## See Also

- [func setAll(value: ElementType)](perclothvertexdata/setall(value:).md)
  Sets the data for all vertices to a common value.
- [func reset()](perclothvertexdata/reset-1nlsc.md)
  Resets the per-vertex data of each vertex to the default position constraint.
- [func reset()](perclothvertexdata/reset-403m8.md)
  Resets the per-vertex data of each vertex to a zero-force external force.
- [func reset()](perclothvertexdata/reset-4x5xi.md)
  Resets the per-vertex data of each vertex to the default motion type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perclothvertexdata/set(vertexindices:value:))*