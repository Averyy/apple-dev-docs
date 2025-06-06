# convert(_:toPointTo:)

**Framework**: MapKit  
**Kind**: method

Converts a map coordinate to a point in the specified view.

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
func convert(_ coordinate: CLLocationCoordinate2D, toPointTo view: NSView?) -> CGPoint
```

#### Return Value

The point (in the appropriate view or window coordinate system) corresponding to the specified latitude and longitude value.

## Parameters

- `coordinate`: The map coordinate that you want to find the corresponding point for.
- `view`: The view where you want to locate the specified map coordinate. If this parameter is  , the method specifies the returned point in the window’s coordinate system. If   isn’t  , the point belongs to the same window as the map view.

## See Also

- [func convert(CGPoint, toCoordinateFrom: UIView?) -> CLLocationCoordinate2D](mkmapview/convert(_:tocoordinatefrom:).md)
  Converts a point in the specified view’s coordinate system to a map coordinate.
- [func convert(MKCoordinateRegion, toRectTo: UIView?) -> CGRect](mkmapview/convert(_:torectto:).md)
  Converts a map region to a rectangle in the specified view.
- [func convert(CGRect, toRegionFrom: UIView?) -> MKCoordinateRegion](mkmapview/convert(_:toregionfrom:).md)
  Converts a rectangle in the specified view’s coordinate system to a map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:topointto:))*