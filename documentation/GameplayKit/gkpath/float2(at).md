# float2(at:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Returns the 2D point at the specified index in the path’s list of vertices.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func float2(at index: Int) -> vector_float2
```

```objc
- (vector_float2) float2AtIndex:(NSUInteger) index;
```

#### Return Value

The vertex at the specified index.

#### Discussion

You define a path’s vertices when creating it, either directly with the [`initWithFloat3Points:count:radius:cyclical:`](./initwithfloat3points_count_radius_cyclical_.md) initializer or indirectly with the [`init(graphNodes:radius:)`](./init%28graphnodes,radius%29.md) initializer.

If the path is a 3D path, this method is still functional but returns only 2D vectors, ignoring the z-component of each point on the path.

## Parameters

- `index`: The index of the vertex to return, between `0` and the [`numPoints`](./numpoints.md) value.

## See Also

### Inspecting a Path’s Shape
- [var numPoints: Int](./numpoints.md)
  The number of vertices in the path.
- [func float3(at: Int) -> vector_float3](./float3%28at%29.md)
  Returns the 3D point at the specified index in the path’s list of vertices.
- [func point(at: Int) -> vector_float2](./point%28at%29.md)
  Returns the 2D point at the specified index in the path’s list of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpath/float2(at:))*