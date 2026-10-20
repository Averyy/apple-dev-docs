# symbol(symbol:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Sets a SwiftUI view to use as the symbol for the chart content.

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
func symbol<V>(@ViewBuilder symbol: () -> V) -> some ChartContent where V : View
```

## Parameters

- `symbol`: The view to use as the plotting symbol.

## See Also

### Setting symbol appearance
- [func symbol<S>(S) -> some ChartContent](./symbol%28_%29.md)
  Sets a plotting symbol type for the chart content.
- [func symbolSize(CGSize) -> some ChartContent](./symbolsize%28_%29-7s0vk.md)
  Sets the plotting symbol size for the chart content.
- [func symbolSize(CGFloat) -> some ChartContent](./symbolsize%28_%29-8dtyt.md)
  Sets the plotting symbol size for the chart content according to a perceived area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/symbol(symbol:))*