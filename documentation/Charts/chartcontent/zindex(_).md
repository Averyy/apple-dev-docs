# zIndex(_:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

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

- `value`: A relative front-to-back ordering for this view; the default is `0`.

## See Also

### Layering chart content
- [func compositingLayer() -> some ChartContent](./compositinglayer%28%29.md)
- [func compositingLayer<V>(style: (PlaceholderContentView<Self>) -> V) -> some ChartContent](./compositinglayer%28style%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/zindex(_:))*