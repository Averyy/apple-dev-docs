# gridOrigin

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The lowest x- and y-coordinates that appear in the grid.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var gridOrigin: vector_int2 { get }
```

```objc
@property (nonatomic, readonly) vector_int2 gridOrigin;
```

## Discussion

You specify origin, width, and height when creating a grid graph with the [`init(fromGridStartingAt:width:height:diagonalsAllowed:)`](./init%28fromgridstartingat,width,height,diagonalsallowed%29.md) initializer. After initialization, you can use this property to examine the parameters the graph was created with—for example, to draw the grid as a debugging overlay in your game UI.

## See Also

### Inspecting a Graph
- [var diagonalsAllowed: Bool](./diagonalsallowed.md)
  A Boolean value that indicates whether nodes in the grid are connected to their diagonal neighbors.
- [var gridWidth: Int](./gridwidth.md)
  The number of possible x-coordinates in the grid.
- [var gridHeight: Int](./gridheight.md)
  The number of possible y-coordinates in the grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/gridorigin)*