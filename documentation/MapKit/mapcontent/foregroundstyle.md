# foregroundStyle(_:)

**Framework**: MapKit  
**Kind**: method

Specifies the shape style used to fill content in drawing map overlays.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func foregroundStyle(_ content: some ShapeStyle) -> some MapContent
```

#### Return Value

Returns [`MapContent`](mapcontent.md) with the foreground style you specified.

## Parameters

- `content`: The shape style to apply to the overlay.

## See Also

- [func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(_:linewidth:).md)
  Applies the given shape style to drawn map overlays using the line width you specify.
- [func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent](mapcontent/stroke(_:style:).md)
  Applies the given shape style to drawn map overlays using the stroke style you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(linewidth:).md)
  Applies the given stoke drawn map overlays using the line width you specify.
- [func strokeStyle(style: StrokeStyle) -> some MapContent](mapcontent/strokestyle(style:).md)
  Applies the given stroke style to drawn map overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/foregroundstyle(_:))*