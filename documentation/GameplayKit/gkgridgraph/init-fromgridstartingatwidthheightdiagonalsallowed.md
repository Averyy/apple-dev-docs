# init(fromGridStartingAt:width:height:diagonalsAllowed:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a graph that describes an integer grid with the specified dimensions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(fromGridStartingAt position: vector_int2, width: Int32, height: Int32, diagonalsAllowed: Bool)
```

#### Return Value

A new grid graph.

#### Discussion

All connections created through this method are bidirectional.

## Parameters

- `position`: The lowest x- and y-coordinates to appear in the grid.
- `width`: The number of possible x-coordinates in the grid.
- `height`: The number of possible y-coordinates in the grid.
- `diagonalsAllowed`:   to connect nodes in the grid to their diagonal neighbors;   to connect nodes only to their horizontal and vertical neighbors.

## See Also

- [init(fromGridStartingAt: vector_int2, width: Int32, height: Int32, diagonalsAllowed: Bool, nodeClass: AnyClass)](gkgridgraph/init(fromgridstartingat:width:height:diagonalsallowed:nodeclass:).md)
  Initializes a graph that describes an integer grid with the specified dimensions, using the specified node class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/init(fromgridstartingat:width:height:diagonalsallowed:))*