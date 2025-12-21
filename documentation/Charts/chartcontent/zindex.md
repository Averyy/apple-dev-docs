# zIndex(_:)

**Framework**: Swift Charts  
**Kind**: method

Controls the display order of overlapping chart content.

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
func zIndex(_ value: Double) -> some ChartContent
```

## Parameters

- `value`: A relative front-to-back ordering for this view; the default is  .

## See Also

- [func compositingLayer() -> some ChartContent](chartcontent/compositinglayer.md)
- [func compositingLayer<V>(style: (PlaceholderContentView<Self>) -> V) -> some ChartContent](chartcontent/compositinglayer(style:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/zindex(_:))*