# alignsMarkStylesWithPlotArea(_:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Aligns this item’s styles with the chart’s plot area.

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
func alignsMarkStylesWithPlotArea(_ aligns: Bool = true) -> some ChartContent
```

#### Discussion

Marks map unit-point coordinates within the plot area’s bounds.

## Parameters

- `aligns`: A Boolean value that indicates whether to align this item’s styles with the plotting area.

## See Also

### Positioning marks
- [func offset(CGSize) -> some ChartContent](./offset%28_%29.md)
  Applies an offset that you specify as a size to the chart content.
- [func offset(x: CGFloat, y: CGFloat) -> some ChartContent](./offset%28x,y%29.md)
  Applies a vertical and horizontal offset to the chart content.
- [func offset(x: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](./offset%28x,ystart,yend%29.md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, y: CGFloat) -> some ChartContent](./offset%28xstart,xend,y%29.md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](./offset%28xstart,xend,ystart,yend%29.md)
  Applies an offset to the chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/alignsmarkstyleswithplotarea(_:))*