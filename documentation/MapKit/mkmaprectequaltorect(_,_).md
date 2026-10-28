# MKMapRectEqualToRect(_:_:)

**Framework**: MapKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether two map rectangles are equal.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func MKMapRectEqualToRect(_ rect1: MKMapRect, _ rect2: MKMapRect) -> Bool
```

```c
static BOOL MKMapRectEqualToRect(MKMapRect rect1, MKMapRect rect2);
```

## Return Value

[`true`](../Swift/true.md) if the rectangles are exactly the same, or [`false`](../Swift/false.md) if the origin point or size values are different.

## Parameters

- `rect1`: The first map rectangle.
- `rect2`: The second map rectangle.

## See Also

### Comparing rectangles
- [var isNull: Bool](./mkmaprect/isnull.md)
  A Boolean value that indicates whether the specified rectangle is null.
- [var isEmpty: Bool](./mkmaprect/isempty.md)
  A Boolean value that indicates whether the specified rectangle has no area.
- [var spans180thMeridian: Bool](./mkmaprect/spans180thmeridian.md)
  A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.
- [var remainder: MKMapRect](./mkmaprect/remainder.md)
  A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprectequaltorect(_:_:))*