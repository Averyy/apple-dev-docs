# stroke(_:style:)

**Framework**: MapKit  
**Kind**: method

Applies the given shape style to drawn map overlays using the stroke style you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
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

- [func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(_:linewidth:).md)
  Applies the given shape style to drawn map overlays using the line width you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(linewidth:).md)
  Applies the given stoke drawn map overlays using the line width you specify.
- [func strokeStyle(style: StrokeStyle) -> some MapContent](mapcontent/strokestyle(style:).md)
  Applies the given stroke style to drawn map overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/stroke(_:style:))*