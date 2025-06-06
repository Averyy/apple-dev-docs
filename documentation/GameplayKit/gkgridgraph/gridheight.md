# gridHeight

**Framework**: GameplayKit  
**Kind**: property

The number of possible y-coordinates in the grid.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var gridHeight: Int { get }
```

#### Discussion

You specify origin, width, and height when creating a grid graph with the [`init(fromGridStartingAt:width:height:diagonalsAllowed:)`](gkgridgraph/init(fromgridstartingat:width:height:diagonalsallowed:).md) initializer. After initialization, you can use this property to examine the parameters the graph was created with—for example, to draw the grid as a debugging overlay in your game UI.

## See Also

- [var diagonalsAllowed: Bool](gkgridgraph/diagonalsallowed.md)
  A Boolean value that indicates whether nodes in the grid are connected to their diagonal neighbors.
- [var gridOrigin: vector_int2](gkgridgraph/gridorigin.md)
  The lowest x- and y-coordinates that appear in the grid.
- [var gridWidth: Int](gkgridgraph/gridwidth.md)
  The number of possible x-coordinates in the grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/gridheight)*