# convert(_:to:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Converts a map coordinate to a point in the specified coordinate space.

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
func convert(_ coordinate: CLLocationCoordinate2D, to space: some CoordinateSpaceProtocol) -> CGPoint?
```

#### Return Value

Returns a [`CGPoint`](../../CoreFoundation/cgpoint.md); otherwise `nil`, if `coordinate` isn’t represented by a point in the [`MapReader`](../mapreader.md) associated with a [`Map`](../map.md).

## Parameters

- `coordinate`: The map coordinate to find the corresponding point for.
- `space`: The reference coordinate space for the returned point.

## See Also

### Converting between coordinate spaces
- [func convert(CGPoint, from: some CoordinateSpaceProtocol) -> CLLocationCoordinate2D?](./convert%28_,from%29.md)
  Converts a point in the specified coordinate space to a map coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapproxy/convert(_:to:))*