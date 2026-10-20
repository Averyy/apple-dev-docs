# convert(_:toCoordinateFrom:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Converts a point in the specified view’s coordinate system to a map coordinate.

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
func convert(_ point: CGPoint, toCoordinateFrom view: UIView?) -> CLLocationCoordinate2D
```

*macOS*

```swift
func convert(_ point: CGPoint, toCoordinateFrom view: NSView?) -> CLLocationCoordinate2D
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (CLLocationCoordinate2D) convertPoint:(CGPoint) point toCoordinateFromView:(UIView *) view;
```

*macOS*

```objc
- (CLLocationCoordinate2D) convertPoint:(CGPoint) point toCoordinateFromView:(NSView *) view;
```

#### Return Value

The map coordinate at the specified point.

## Parameters

- `point`: The point you want to convert.
- `view`: The view that serves as the reference coordinate system for the `point` parameter.

## See Also

### Converting map coordinates
- [func convert(CLLocationCoordinate2D, toPointTo: UIView?) -> CGPoint](./convert%28_,topointto%29.md)
  Converts a map coordinate to a point in the specified view.
- [func convert(MKCoordinateRegion, toRectTo: UIView?) -> CGRect](./convert%28_,torectto%29.md)
  Converts a map region to a rectangle in the specified view.
- [func convert(CGRect, toRegionFrom: UIView?) -> MKCoordinateRegion](./convert%28_,toregionfrom%29.md)
  Converts a rectangle in the specified view’s coordinate system to a map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:tocoordinatefrom:))*