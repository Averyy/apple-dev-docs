# convert(_:toRegionFrom:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Converts a rectangle in the specified view’s coordinate system to a map region.

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
func convert(_ rect: CGRect, toRegionFrom view: UIView?) -> MKCoordinateRegion
```

*macOS*

```swift
func convert(_ rect: CGRect, toRegionFrom view: NSView?) -> MKCoordinateRegion
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (MKCoordinateRegion) convertRect:(CGRect) rect toRegionFromView:(UIView *) view;
```

*macOS*

```objc
- (MKCoordinateRegion) convertRect:(CGRect) rect toRegionFromView:(NSView *) view;
```

#### Return Value

The map region corresponding to the specified view rectangle.

## Parameters

- `rect`: The rectangle you want to convert.
- `view`: The view that serves as the reference coordinate system for the `rect` parameter.

## See Also

### Converting map coordinates
- [func convert(CLLocationCoordinate2D, toPointTo: UIView?) -> CGPoint](./convert%28_,topointto%29.md)
  Converts a map coordinate to a point in the specified view.
- [func convert(CGPoint, toCoordinateFrom: UIView?) -> CLLocationCoordinate2D](./convert%28_,tocoordinatefrom%29.md)
  Converts a point in the specified view’s coordinate system to a map coordinate.
- [func convert(MKCoordinateRegion, toRectTo: UIView?) -> CGRect](./convert%28_,torectto%29.md)
  Converts a map region to a rectangle in the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:toregionfrom:))*