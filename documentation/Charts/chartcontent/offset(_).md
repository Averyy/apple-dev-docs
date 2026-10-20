# offset(_:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Applies an offset that you specify as a size to the chart content.

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
func offset(_ value: CGSize) -> some ChartContent
```

## Parameters

- `value`: The offset distance in screen coordinates.

## See Also

### Positioning marks
- [func offset(x: CGFloat, y: CGFloat) -> some ChartContent](./offset%28x,y%29.md)
  Applies a vertical and horizontal offset to the chart content.
- [func offset(x: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](./offset%28x,ystart,yend%29.md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, y: CGFloat) -> some ChartContent](./offset%28xstart,xend,y%29.md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](./offset%28xstart,xend,ystart,yend%29.md)
  Applies an offset to the chart content.
- [func alignsMarkStylesWithPlotArea(Bool) -> some ChartContent](./alignsmarkstyleswithplotarea%28_%29.md)
  Aligns this item’s styles with the chart’s plot area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/offset(_:))*