# isNull

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the specified rectangle is null.

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
var isNull: Bool { get }
```

#### Discussion

For this class, a rectangle is `null` if its origin point contains an invalid or infinite value.

## See Also

- [func MKMapRectEqualToRect(MKMapRect, MKMapRect) -> Bool](mkmaprectequaltorect(_:_:).md)
  Returns a Boolean value that indicates whether two map rectangles are equal.
- [var isEmpty: Bool](mkmaprect/isempty.md)
  A Boolean value that indicates whether the specified rectangle has no area.
- [var spans180thMeridian: Bool](mkmaprect/spans180thmeridian.md)
  A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.
- [var remainder: MKMapRect](mkmaprect/remainder.md)
  A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/isnull)*