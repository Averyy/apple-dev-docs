# camera(framing:allowPitch:)

**Framework**: MapKit  
**Kind**: method

Creates a camera in the context of the map that frames the given map item.

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
func camera(framing item: MKMapItem, allowPitch: Bool = true) -> MapCamera
```

#### Return Value

Returns a [`MapCamera`](mapcamera.md) with the framing region and pitch you specified.

## Parameters

- `item`: The   to frame.
- `allowPitch`: A Boolean value that indicates whether you can pitch the camera to frame the content.

## See Also

- [func camera(framing: MKCoordinateRegion) -> MapCamera](mapproxy/camera(framing:)-1asl2.md)
  Creates a camera in the context of the map that frames the given coordinate region.
- [func camera(framing: MKMapRect) -> MapCamera](mapproxy/camera(framing:)-uxov.md)
  Creates a camera in the context of the map that frames the given map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapproxy/camera(framing:allowpitch:))*