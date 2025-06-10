# convert(_:from:)

**Framework**: MapKit  
**Kind**: method

Converts a point in the specified coordinate space to a map coordinate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
func convert(_ point: CGPoint, from space: some CoordinateSpaceProtocol) -> CLLocationCoordinate2D?
```

#### Return Value

Returns a doc://com.apple.documentation/documentation/corelocation/cllocationcoordinate2d; or `nil,` if the specified `point` isn’t represented by a point in the [`MapReader`](mapreader.md) associated with a [`Map`](map.md).

## Parameters

- `point`: The point to convert.
- `space`: The reference coordinate space for  .

## See Also

- [func convert(CLLocationCoordinate2D, to: some CoordinateSpaceProtocol) -> CGPoint?](mapproxy/convert(_:to:).md)
  Converts a map coordinate to a point in the specified coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapproxy/convert(_:from:))*