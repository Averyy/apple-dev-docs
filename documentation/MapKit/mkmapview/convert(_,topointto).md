# convert(_:toPointTo:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Converts a map coordinate to a point in the specified view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func convert(_ coordinate: CLLocationCoordinate2D, toPointTo view: UIView?) -> CGPoint
```

*macOS*

```swift
func convert(_ coordinate: CLLocationCoordinate2D, toPointTo view: NSView?) -> CGPoint
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (CGPoint) convertCoordinate:(CLLocationCoordinate2D) coordinate toPointToView:(UIView *) view;
```

*macOS*

```objc
- (CGPoint) convertCoordinate:(CLLocationCoordinate2D) coordinate toPointToView:(NSView *) view;
```

## Return Value

The point (in the appropriate view or window coordinate system) corresponding to the specified latitude and longitude value.

## Parameters

- `coordinate`: The map coordinate that you want to find the corresponding point for.
- `view`: The view where you want to locate the specified map coordinate. If this parameter is `nil`, the method specifies the returned point in the window’s coordinate system. If `view` isn’t `nil`, the point belongs to the same window as the map view.

## See Also

### Converting map coordinates
- [func convert(CGPoint, toCoordinateFrom: UIView?) -> CLLocationCoordinate2D](./convert%28_,tocoordinatefrom%29.md)
  Converts a point in the specified view’s coordinate system to a map coordinate.
- [func convert(MKCoordinateRegion, toRectTo: UIView?) -> CGRect](./convert%28_,torectto%29.md)
  Converts a map region to a rectangle in the specified view.
- [func convert(CGRect, toRegionFrom: UIView?) -> MKCoordinateRegion](./convert%28_,toregionfrom%29.md)
  Converts a rectangle in the specified view’s coordinate system to a map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:topointto:))*