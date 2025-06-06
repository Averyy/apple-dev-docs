# float3(at:)

**Framework**: GameplayKit  
**Kind**: method

Returns the 3D point at the specified index in the path’s list of vertices.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func float3(at index: Int) -> vector_float3
```

#### Return Value

The vertex at the specified index.

#### Discussion

You define a path’s vertices when creating it, either directly with the [`initWithFloat3Points:count:radius:cyclical:`](gkpath/initwithfloat3points:count:radius:cyclical:.md) initializer or indirectly with the [`init(graphNodes:radius:)`](gkpath/init(graphnodes:radius:).md) initializer.

If the path is a 2D path, this method is still functional, but returns 3D vectors whose z-component is always zero.

## Parameters

- `index`: The index of the vertex to return, between   and the   value.

## See Also

- [var numPoints: Int](gkpath/numpoints.md)
  The number of vertices in the path.
- [func float2(at: Int) -> vector_float2](gkpath/float2(at:).md)
  Returns the 2D point at the specified index in the path’s list of vertices.
- [func point(at: Int) -> vector_float2](gkpath/point(at:).md)
  Returns the 2D point at the specified index in the path’s list of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpath/float3(at:))*