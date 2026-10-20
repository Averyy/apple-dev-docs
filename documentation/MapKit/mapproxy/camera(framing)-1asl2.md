# camera(framing:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Creates a camera in the context of the map that frames the given coordinate region.

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
func camera(framing region: MKCoordinateRegion) -> MapCamera
```

#### Return Value

Returns a [`MapCamera`](../mapcamera.md) with the framing region you specified.

## Parameters

- `region`: The coordinate region to frame.

## See Also

### Creating a camera proxy
- [func camera(framing: MKMapRect) -> MapCamera](./camera%28framing%29-uxov.md)
  Creates a camera in the context of the map that frames the given map rectangle.
- [func camera(framing: MKMapItem, allowPitch: Bool) -> MapCamera](./camera%28framing,allowpitch%29.md)
  Creates a camera in the context of the map that frames the given map item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapproxy/camera(framing:)-1asl2)*