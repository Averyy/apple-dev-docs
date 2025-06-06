# offset(xStart:xEnd:y:)

**Framework**: Swift Charts  
**Kind**: method

Applies an offset to the chart content.

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
func offset(xStart: CGFloat = 0, xEnd: CGFloat = 0, y: CGFloat = 0) -> some ChartContent
```

#### Discussion

The `xStart` and `xEnd` offset values apply only to marks that have such properties, like bar marks and line segment marks.

## Parameters

- `xStart`: The starting horizontal offset in screen coordinates.
- `xEnd`: The ending horizontal offset in screen coordinates.
- `y`: The vertical offset in screen coordinates.

## See Also

- [func offset(CGSize) -> some ChartContent](chartcontent/offset(_:).md)
  Applies an offset that you specify as a size to the chart content.
- [func offset(x: CGFloat, y: CGFloat) -> some ChartContent](chartcontent/offset(x:y:).md)
  Applies a vertical and horizontal offset to the chart content.
- [func offset(x: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](chartcontent/offset(x:ystart:yend:).md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](chartcontent/offset(xstart:xend:ystart:yend:).md)
  Applies an offset to the chart content.
- [func alignsMarkStylesWithPlotArea(Bool) -> some ChartContent](chartcontent/alignsmarkstyleswithplotarea(_:).md)
  Aligns this item’s styles with the chart’s plot area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/offset(xstart:xend:y:))*