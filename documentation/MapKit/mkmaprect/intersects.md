# intersects(_:)

**Framework**: MapKit  
**Kind**: method

Returns a Boolean value that indicates whether two rectangles intersect each other.

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
func intersects(_ rect2: MKMapRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `rect1` and `rect2` intersect each other, or [`false`](https://developer.apple.com/documentation/swift/false) if they don’t intersect or either rectangle is `null`.

#### Discussion

The rectangles aren’t intersecting if the only intersection occurs along an edge. For a true intersection, the rectangles both need to enclose a single rectangular area with a width and height that are both greater than `0`.

## Parameters

- `rect2`: The second rectangle.

## See Also

- [func contains(MKMapPoint) -> Bool](mkmaprect/contains(_:)-79tjt.md)
  Returns a Boolean value that indicates whether the specified map point lies within the rectangle.
- [func contains(MKMapRect) -> Bool](mkmaprect/contains(_:)-1z5oa.md)
  Returns a Boolean value that indicates whether one rectangle contains another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/intersects(_:))*