# convert(_:toRectTo:)

**Framework**: MapKit  
**Kind**: method

Converts a map region to a rectangle in the specified view.

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
func convert(_ region: MKCoordinateRegion, toRectTo view: UIView?) -> CGRect
```

#### Return Value

The rectangle corresponding to the specified map region.

## Parameters

- `region`: The map region that you want to find the corresponding view rectangle for.
- `view`: The view where you want to locate the specified map region. If this parameter is  , the method specifies the returned rectangle in the window’s coordinate system. If   isn’t  , the rectangle belongs to the same window as the map view.

## See Also

- [func convert(CLLocationCoordinate2D, toPointTo: UIView?) -> CGPoint](mkmapview/convert(_:topointto:).md)
  Converts a map coordinate to a point in the specified view.
- [func convert(CGPoint, toCoordinateFrom: UIView?) -> CLLocationCoordinate2D](mkmapview/convert(_:tocoordinatefrom:).md)
  Converts a point in the specified view’s coordinate system to a map coordinate.
- [func convert(CGRect, toRegionFrom: UIView?) -> MKCoordinateRegion](mkmapview/convert(_:toregionfrom:).md)
  Converts a rectangle in the specified view’s coordinate system to a map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:torectto:))*