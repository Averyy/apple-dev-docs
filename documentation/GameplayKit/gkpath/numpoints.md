# numPoints

**Framework**: GameplayKit  
**Kind**: property

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

#### Discussion

You define a path’s vertices when creating it, either directly with the [`initWithPoints:count:radius:cyclical:`](gkpath/initwithpoints:count:radius:cyclical:.md) initializer or indirectly with the [`init(graphNodes:radius:)`](gkpath/init(graphnodes:radius:).md) initializer.

## See Also

- [func float2(at: Int) -> vector_float2](gkpath/float2(at:).md)
  Returns the 2D point at the specified index in the path’s list of vertices.
- [func float3(at: Int) -> vector_float3](gkpath/float3(at:).md)
  Returns the 3D point at the specified index in the path’s list of vertices.
- [func point(at: Int) -> vector_float2](gkpath/point(at:).md)
  Returns the 2D point at the specified index in the path’s list of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpath/numpoints)*