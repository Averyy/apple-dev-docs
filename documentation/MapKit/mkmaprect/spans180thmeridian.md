# spans180thMeridian

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var spans180thMeridian: Bool { get }
```

```c
extern BOOL MKMapRectSpans180thMeridian(MKMapRect rect);
```

## See Also

### Comparing rectangles
- [var isNull: Bool](./isnull.md)
  A Boolean value that indicates whether the specified rectangle is null.
- [func MKMapRectEqualToRect(MKMapRect, MKMapRect) -> Bool](../mkmaprectequaltorect%28_,_%29.md)
  Returns a Boolean value that indicates whether two map rectangles are equal.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the specified rectangle has no area.
- [var remainder: MKMapRect](./remainder.md)
  A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/spans180thmeridian)*