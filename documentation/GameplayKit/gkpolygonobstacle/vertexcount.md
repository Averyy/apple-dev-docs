# vertexCount

**Framework**: GameplayKit  
**Kind**: property

The number of vertices that define the polygon-shaped area of the obstacle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var vertexCount: Int { get }
```

#### Discussion

Obstacles are immutable objects; to change the shape of an obstacle, remove it and create a new obstacle with a new list of vertices. Use this property along with the [`vertex(at:)`](gkpolygonobstacle/vertex(at:).md) method to inspect an existing obstacle—for example, to draw a debugging overlay representing the obstacle in your game.

## See Also

- [func vertex(at: Int) -> vector_float2](gkpolygonobstacle/vertex(at:).md)
  Returns the point coordinates of the specified vertex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpolygonobstacle/vertexcount)*