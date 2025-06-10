# convert(_:toCoordinateFrom:)

**Framework**: MapKit  
**Kind**: method

Converts a point in the specified view’s coordinate system to a map coordinate.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func convert(_ point: CGPoint, toCoordinateFrom view: UIView?) -> CLLocationCoordinate2D
```

#### Return Value

The map coordinate at the specified point.

## Parameters

- `point`: The point you want to convert.
- `view`: The view that serves as the reference coordinate system for the   parameter.

## See Also

- [func convert(CLLocationCoordinate2D, toPointTo: UIView?) -> CGPoint](mkmapview/convert(_:topointto:).md)
  Converts a map coordinate to a point in the specified view.
- [func convert(MKCoordinateRegion, toRectTo: UIView?) -> CGRect](mkmapview/convert(_:torectto:).md)
  Converts a map region to a rectangle in the specified view.
- [func convert(CGRect, toRegionFrom: UIView?) -> MKCoordinateRegion](mkmapview/convert(_:toregionfrom:).md)
  Converts a rectangle in the specified view’s coordinate system to a map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:tocoordinatefrom:))*