# init(polyline:)

**Framework**: MapKit  
**Kind**: init

Creates a new overlay view using the specified polyline overlay object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
init(polyline: MKPolyline)
```

#### Return Value

An initialized polyline renderer object.

## Parameters

- `polyline`: The polyline overlay containing information about the area the renderer draws. This object requires at least two points defining the line segment to draw. This parameter can’t be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/init(polyline:))*