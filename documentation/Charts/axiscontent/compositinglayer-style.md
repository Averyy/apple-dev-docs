# compositingLayer(style:)

**Framework**: Swift Charts  
**Kind**: method

Creates a compositing layer for the chart content, and apply view modifiers to the compositing layer.

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
func compositingLayer<V>(@ViewBuilder style: (PlaceholderContentView<Self>) -> V) -> some AxisContent where V : View
```

## Parameters

- `style`: A closure that applies view modifiers to the compositing layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axiscontent/compositinglayer(style:))*