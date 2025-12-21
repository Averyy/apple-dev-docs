# compositingLayer(style:)

**Framework**: Swift Charts  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func compositingLayer<V>(style: (PlaceholderContentView<Self>) -> V) -> some ChartContent where V : View
```

## See Also

- [func compositingLayer() -> some ChartContent](chartcontent/compositinglayer.md)
- [func zIndex(Double) -> some ChartContent](chartcontent/zindex(_:).md)
  Controls the display order of overlapping chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/compositinglayer(style:))*