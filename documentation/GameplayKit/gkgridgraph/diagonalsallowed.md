# diagonalsAllowed

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL diagonalsAllowed;
```

## Discussion

If this property’s value is [`true`](../../Swift/true.md), nodes in the grid are connected to their diagonal neighbors. If the value is [`false`](../../Swift/false.md), nodes are connected only to their horizontal and vertical neighbors.

You specify this option when creating a grid graph with the [`init(fromGridStartingAt:width:height:diagonalsAllowed:)`](./init%28fromgridstartingat,width,height,diagonalsallowed%29.md) initializer. After initialization, you can use this property to examine the parameters the graph was created with—for example, to draw the grid as a debugging overlay in your game UI.

## See Also

### Inspecting a Graph
- [var gridOrigin: vector_int2](./gridorigin.md)
  The lowest x- and y-coordinates that appear in the grid.
- [var gridWidth: Int](./gridwidth.md)
  The number of possible x-coordinates in the grid.
- [var gridHeight: Int](./gridheight.md)
  The number of possible y-coordinates in the grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/diagonalsallowed)*