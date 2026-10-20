# clipShape(_:style:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Sets a clip shape for the chart content.

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
func clipShape(_ shape: some Shape, style: FillStyle = FillStyle()) -> some ChartContent
```

## Parameters

- `shape`: The clip shape. The shape fills each mark’s frame.
- `style`: The fill to use when rasterizing the shape.

## See Also

### Masking and clipping
- [func mask<C>(content: () -> C) -> some ChartContent](./mask%28content%29.md)
  Masks chart content using the alpha channel of the specified content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/clipshape(_:style:))*