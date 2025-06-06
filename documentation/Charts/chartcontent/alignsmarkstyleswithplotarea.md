# alignsMarkStylesWithPlotArea(_:)

**Framework**: Swift Charts  
**Kind**: method

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

- `aligns`: A Boolean value that indicates whether to align   this item’s styles with the plotting area.

## See Also

- [func offset(CGSize) -> some ChartContent](chartcontent/offset(_:).md)
  Applies an offset that you specify as a size to the chart content.
- [func offset(x: CGFloat, y: CGFloat) -> some ChartContent](chartcontent/offset(x:y:).md)
  Applies a vertical and horizontal offset to the chart content.
- [func offset(x: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](chartcontent/offset(x:ystart:yend:).md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, y: CGFloat) -> some ChartContent](chartcontent/offset(xstart:xend:y:).md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](chartcontent/offset(xstart:xend:ystart:yend:).md)
  Applies an offset to the chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/alignsmarkstyleswithplotarea(_:))*