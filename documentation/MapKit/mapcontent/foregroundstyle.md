# foregroundStyle(_:)

**Framework**: MapKit  
**Kind**: method

Specifies the shape style used to fill content in drawing map overlays.

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
@preconcurrency func foregroundStyle(_ content: some ShapeStyle) -> some MapContent
```

#### Return Value

Returns [`MapContent`](mapcontent.md) with the foreground style you specified.

## Parameters

- `content`: The shape style to apply to the overlay.

## See Also

- [func tint<S>(S) -> some MapContent](mapcontent/tint(_:).md)
  The tint shape style to apply to map content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/foregroundstyle(_:))*