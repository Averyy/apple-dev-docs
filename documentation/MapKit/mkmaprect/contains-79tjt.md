# contains(_:)

**Framework**: MapKit  
**Kind**: method

Returns a Boolean value that indicates whether the specified map point lies within the rectangle.

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
func contains(_ point: MKMapPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the rectangle isn’t `null` or empty and the point is inside the rectangle; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

For this method, a point is inside the rectangle if its coordinates lie inside the rectangle or on the minimum X or minimum Y edge.

## Parameters

- `point`: The point to check.

## See Also

- [func contains(MKMapRect) -> Bool](mkmaprect/contains(_:)-1z5oa.md)
  Returns a Boolean value that indicates whether one rectangle contains another.
- [func intersects(MKMapRect) -> Bool](mkmaprect/intersects(_:).md)
  Returns a Boolean value that indicates whether two rectangles intersect each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/contains(_:)-79tjt)*