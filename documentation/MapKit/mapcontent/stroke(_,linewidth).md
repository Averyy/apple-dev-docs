# stroke(_:lineWidth:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Applies the given shape style to drawn map overlays using the line width you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func stroke(_ content: some ShapeStyle, lineWidth: CGFloat = 1) -> some MapContent
```

#### Return Value

Returns [`MapContent`](../mapcontent.md) drawn with the [`ShapeStyle`](../../SwiftUI/shapestyle.md) and `lineWidth` you specified.

## Parameters

- `content`: The shape style to apply.
- `lineWidth`: The line width to draw the stroke with.

## See Also

### Styling the circle
- [func foregroundStyle(some ShapeStyle) -> some MapContent](./foregroundstyle%28_%29.md)
  Specifies the shape style used to fill content in drawing map overlays.
- [func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent](./stroke%28_,style%29.md)
  Applies the given shape style to drawn map overlays using the stroke style you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](./stroke%28linewidth%29.md)
  Applies the given stoke drawn map overlays using the line width you specify.
- [func strokeStyle(style: StrokeStyle) -> some MapContent](./strokestyle%28style%29.md)
  Applies the given stroke style to drawn map overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/stroke(_:linewidth:))*