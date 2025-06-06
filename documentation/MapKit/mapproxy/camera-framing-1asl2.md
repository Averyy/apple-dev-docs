# camera(framing:)

**Framework**: MapKit  
**Kind**: method

Creates a camera in the context of the map that frames the given coordinate region.

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
func camera(framing region: MKCoordinateRegion) -> MapCamera
```

#### Return Value

Returns a [`MapCamera`](mapcamera.md) with the framing region you specified.

## Parameters

- `region`: The coordinate region to frame.

## See Also

- [func camera(framing: MKMapRect) -> MapCamera](mapproxy/camera(framing:)-uxov.md)
  Creates a camera in the context of the map that frames the given map rectangle.
- [func camera(framing: MKMapItem, allowPitch: Bool) -> MapCamera](mapproxy/camera(framing:allowpitch:).md)
  Creates a camera in the context of the map that frames the given map item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapproxy/camera(framing:)-1asl2)*