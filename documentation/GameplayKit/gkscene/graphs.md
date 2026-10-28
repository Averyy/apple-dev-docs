# graphs

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,GKGraph *> * graphs;
```

## Discussion

When you define pathfinding graphs in the Xcode SpriteKit scene editor, Xcode automatically adds them to this array.

## See Also

### Managing Pathfinding Graphs
- [func removeGraph(String)](./removegraph%28_%29.md)
  Removes a pathfinding graph from the list of graphs managed by the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkscene/graphs)*