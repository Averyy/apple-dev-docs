# contains(_:)

**Framework**: MapKit  
**Kind**: method

Returns a Boolean value that indicates whether one rectangle contains another.

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
func contains(_ rect2: MKMapRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `rect2` is `null` or lies entirely inside `rect1`; otherwise, returns [`false`](https://developer.apple.com/documentation/swift/false) if `rect1` is `null` or doesn’t completely enclose `rect2`.

## Parameters

- `rect2`: The rectangle that   might contain.

## See Also

- [func contains(MKMapPoint) -> Bool](mkmaprect/contains(_:)-79tjt.md)
  Returns a Boolean value that indicates whether the specified map point lies within the rectangle.
- [func intersects(MKMapRect) -> Bool](mkmaprect/intersects(_:).md)
  Returns a Boolean value that indicates whether two rectangles intersect each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/contains(_:)-1z5oa)*