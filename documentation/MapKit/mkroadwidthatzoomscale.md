# MKRoadWidthAtZoomScale(_:)

**Framework**: MapKit  
**Kind**: func

Returns the width (in screen points) of roads on a map at the specified zoom level.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func MKRoadWidthAtZoomScale(_ zoomScale: MKZoomScale) -> CGFloat
```

#### Return Value

The width of roads, measured in screen points. You can use the returned value to set the width of lines in drawing code that traces the path of a road.

## Parameters

- `zoomScale`: The scale factor currently applied to the map view.

## See Also

- [typealias MKZoomScale](mkzoomscale.md)
  A scale factor to use in conjunction with a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroadwidthatzoomscale(_:))*