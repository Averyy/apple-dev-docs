# diagonalsAllowed

**Framework**: GameplayKit  
**Kind**: property

A Boolean value that indicates whether nodes in the grid are connected to their diagonal neighbors.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var diagonalsAllowed: Bool { get }
```

#### Discussion

If this property’s value is [`true`](https://developer.apple.com/documentation/Swift/true), nodes in the grid are connected to their diagonal neighbors. If the value is [`false`](https://developer.apple.com/documentation/Swift/false), nodes are connected only to their horizontal and vertical neighbors.

You specify this option when creating a grid graph with the [`init(fromGridStartingAt:width:height:diagonalsAllowed:)`](gkgridgraph/init(fromgridstartingat:width:height:diagonalsallowed:).md) initializer. After initialization, you can use this property to examine the parameters the graph was created with—for example, to draw the grid as a debugging overlay in your game UI.

## See Also

- [var gridOrigin: vector_int2](gkgridgraph/gridorigin.md)
  The lowest x- and y-coordinates that appear in the grid.
- [var gridWidth: Int](gkgridgraph/gridwidth.md)
  The number of possible x-coordinates in the grid.
- [var gridHeight: Int](gkgridgraph/gridheight.md)
  The number of possible y-coordinates in the grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/diagonalsallowed)*