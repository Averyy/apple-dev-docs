# numPoints

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The number of vertices in the path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var numPoints: Int { get }
```

```objc
@property (readonly) NSUInteger numPoints;
```

#### Discussion

You define a path’s vertices when creating it, either directly with the [`initWithPoints:count:radius:cyclical:`](./initwithpoints_count_radius_cyclical_.md) initializer or indirectly with the [`init(graphNodes:radius:)`](./init%28graphnodes,radius%29.md) initializer.

## See Also

### Inspecting a Path’s Shape
- [func float2(at: Int) -> vector_float2](./float2%28at%29.md)
  Returns the 2D point at the specified index in the path’s list of vertices.
- [func float3(at: Int) -> vector_float3](./float3%28at%29.md)
  Returns the 3D point at the specified index in the path’s list of vertices.
- [func point(at: Int) -> vector_float2](./point%28at%29.md)
  Returns the 2D point at the specified index in the path’s list of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpath/numpoints)*