# symbolSize(_:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Sets the plotting symbol size for the chart content according to a perceived area.

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
func symbolSize(_ area: CGFloat) -> some ChartContent
```

## Parameters

- `area`: The perceived area in square points. For example, a square with 10 points on each side has an area of 100 square points.

## See Also

### Setting symbol appearance
- [func symbol<S>(S) -> some ChartContent](./symbol%28_%29.md)
  Sets a plotting symbol type for the chart content.
- [func symbol<V>(symbol: () -> V) -> some ChartContent](./symbol%28symbol%29.md)
  Sets a SwiftUI view to use as the symbol for the chart content.
- [func symbolSize(CGSize) -> some ChartContent](./symbolsize%28_%29-7s0vk.md)
  Sets the plotting symbol size for the chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/symbolsize(_:)-8dtyt)*