# tint(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

The tint shape style to apply to map content.

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
@preconcurrency func tint<S>(_ tint: S) -> some MapContent where S : ShapeStyle
```

## Return Value

Returns [`MapContent`](../mapcontent.md) with overlays drawn with the [`ShapeStyle`](../../SwiftUI/shapestyle.md) you specified.

## Parameters

- `tint`: The tint to apply.

## See Also

### Setting the content style
- [func foregroundStyle(some ShapeStyle) -> some MapContent](./foregroundstyle%28_%29.md)
  Specifies the shape style used to fill content in drawing map overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/tint(_:))*