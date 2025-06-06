# graphs

**Framework**: GameplayKit  
**Kind**: property

The list of pathfinding graph objects managed by the scene.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var graphs: [String : GKGraph] { get }
```

#### Discussion

When you define pathfinding graphs in the Xcode SpriteKit scene editor, Xcode automatically adds them to this array.

## See Also

- [func removeGraph(String)](gkscene/removegraph(_:).md)
  Removes a pathfinding graph from the list of graphs managed by the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkscene/graphs)*