# strokeStyle(style:)

**Framework**: MapKit  
**Kind**: method

Applies the given stroke style to drawn map overlays.

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
@preconcurrency func strokeStyle(style: StrokeStyle) -> some MapContent
```

#### Return Value

Returns [`MapContent`](mapcontent.md) with overlays drawn with the [`StrokeStyle`](https://developer.apple.com/documentation/SwiftUI/StrokeStyle) you specified.

## Parameters

- `style`: The stroke style to apply.

## See Also

- [func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(_:linewidth:).md)
  Applies the given shape style to drawn map overlays using the line width you specify.
- [func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent](mapcontent/stroke(_:style:).md)
  Applies the given shape style to drawn map overlays using the stroke style you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(linewidth:).md)
  Applies the given stoke drawn map overlays using the line width you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/strokestyle(style:))*