# mask(content:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Masks chart content using the alpha channel of the specified content.

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
func mask<C>(@ContentBuilder content: () -> C) -> some ChartContent where C : ChartContent
```

## Discussion

Parameter content: The content whose alpha will be applied to this item.

## See Also

### Masking and clipping
- [func clipShape(some Shape, style: FillStyle) -> some ChartContent](./clipshape%28_,style%29.md)
  Sets a clip shape for the chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/mask(content:))*