# tint(_:)

**Framework**: MapKit  
**Kind**: method

The tint shape style to apply to map content.

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
@preconcurrency func tint<S>(_ tint: S) -> some MapContent where S : ShapeStyle
```

#### Return Value

Returns [`MapContent`](mapcontent.md) with overlays drawn with the [`ShapeStyle`](https://developer.apple.com/documentation/SwiftUI/ShapeStyle) you specified.

## Parameters

- `tint`: The tint to apply.

## See Also

- [func foregroundStyle(some ShapeStyle) -> some MapContent](mapcontent/foregroundstyle(_:).md)
  Specifies the shape style used to fill content in drawing map overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/tint(_:))*