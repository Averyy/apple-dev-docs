# init(xStart:xEnd:y:height:)

**Framework**: Swift Charts  
**Kind**: init

Creates a rectangle mark with a fixed x interval and y encoding.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<Y>(xStart: CGFloat? = nil, xEnd: CGFloat? = nil, y: PlottableValue<Y>, height: MarkDimension = .automatic) where Y : Plottable
```

#### Discussion

- xStart: The x start position. If `xStart` is `nil` then the rectangle will start at the leading edge of the plotting area.
- xEnd: The x end position. If `xEnd` is `nil` then the rectangle will end at the trailing edge of the plotting area.
- y: The value plotted with y.
- height: The rectangle height.  If `height` is not specified, then 70% of the step size will be used. If there is no step size a default height (in pts) will be used.

##### Discussion

Use this initializer to map a y position to a rectangle for each data element. Optionally, specify the height, xStart position, or xEnd position, of the rectangles.

The example below omits the optional `x`, `width`, and `height` parameters and uses a number scale starting at (0,0) and ending at (6,6). The rectangle has the coordinates: (0,0), (0,3), (6,3), (6,0).

```swift
Chart(data) {
    RectangleMark(
        y: .value("Rect Y", 3)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (0,0), (0,3), (6,3), (6,0).](https://docs-assets.developer.apple.com/published/909a7386624d6d034a15b3f5916107a9/RectangleMarkSwift.RectangleMarkScatterWithRectangleY%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectanglemark/init(xstart:xend:y:height:)-4x46i)*