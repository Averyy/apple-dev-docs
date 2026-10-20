# stroke(_:style:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Applies the given shape style to drawn map overlays using the stroke style you specify.

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
@preconcurrency func stroke(_ content: some ShapeStyle, style: StrokeStyle) -> some MapContent
```

## Parameters

- `content`: The shape style to apply.
- `style`: The stroke style to apply.

## See Also

### Styling the circle
- [func foregroundStyle(some ShapeStyle) -> some MapContent](./foregroundstyle%28_%29.md)
  Specifies the shape style used to fill content in drawing map overlays.
- [func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent](./stroke%28_,linewidth%29.md)
  Applies the given shape style to drawn map overlays using the line width you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](./stroke%28linewidth%29.md)
  Applies the given stoke drawn map overlays using the line width you specify.
- [func strokeStyle(style: StrokeStyle) -> some MapContent](./strokestyle%28style%29.md)
  Applies the given stroke style to drawn map overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/stroke(_:style:))*