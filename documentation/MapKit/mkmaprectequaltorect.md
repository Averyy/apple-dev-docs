# MKMapRectEqualToRect(_:_:)

**Framework**: MapKit  
**Kind**: func

Returns a Boolean value that indicates whether two map rectangles are equal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func MKMapRectEqualToRect(_ rect1: MKMapRect, _ rect2: MKMapRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the rectangles are exactly the same, or [`false`](https://developer.apple.com/documentation/swift/false) if the origin point or size values are different.

## Parameters

- `rect1`: The first map rectangle.
- `rect2`: The second map rectangle.

## See Also

- [var isNull: Bool](mkmaprect/isnull.md)
  A Boolean value that indicates whether the specified rectangle is null.
- [var isEmpty: Bool](mkmaprect/isempty.md)
  A Boolean value that indicates whether the specified rectangle has no area.
- [var spans180thMeridian: Bool](mkmaprect/spans180thmeridian.md)
  A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.
- [var remainder: MKMapRect](mkmaprect/remainder.md)
  A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprectequaltorect(_:_:))*