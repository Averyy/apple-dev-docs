# intersects(_:)

**Framework**: MapKit  
**Kind**: method

Returns a Boolean value that indicates whether the specified rectangle intersects the overlay’s shape.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
optional func intersects(_ mapRect: MKMapRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if any part of the map rectangle intersects the receiver’s shape, or [`false`](https://developer.apple.com/documentation/Swift/false) if it doesn’t.

#### Discussion

You can implement this method to provide more specific bounds-checking for an overlay. If you don’t implement it, the method uses the bounding rectangle to detect intersections.

## Parameters

- `mapRect`: The rectangle to intersect with the overlay’s area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlay/intersects(_:))*