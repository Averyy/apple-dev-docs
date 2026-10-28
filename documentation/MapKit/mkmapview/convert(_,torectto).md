# convert(_:toRectTo:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Converts a map region to a rectangle in the specified view.

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
func convert(_ region: MKCoordinateRegion, toRectTo view: UIView?) -> CGRect
```

*macOS*

```swift
func convert(_ region: MKCoordinateRegion, toRectTo view: NSView?) -> CGRect
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (CGRect) convertRegion:(MKCoordinateRegion) region toRectToView:(UIView *) view;
```

*macOS*

```objc
- (CGRect) convertRegion:(MKCoordinateRegion) region toRectToView:(NSView *) view;
```

## Return Value

The rectangle corresponding to the specified map region.

## Parameters

- `region`: The map region that you want to find the corresponding view rectangle for.
- `view`: The view where you want to locate the specified map region. If this parameter is `nil`, the method specifies the returned rectangle in the window’s coordinate system. If `view` isn’t `nil`, the rectangle belongs to the same window as the map view.

## See Also

### Converting map coordinates
- [func convert(CLLocationCoordinate2D, toPointTo: UIView?) -> CGPoint](./convert%28_,topointto%29.md)
  Converts a map coordinate to a point in the specified view.
- [func convert(CGPoint, toCoordinateFrom: UIView?) -> CLLocationCoordinate2D](./convert%28_,tocoordinatefrom%29.md)
  Converts a point in the specified view’s coordinate system to a map coordinate.
- [func convert(CGRect, toRegionFrom: UIView?) -> MKCoordinateRegion](./convert%28_,toregionfrom%29.md)
  Converts a rectangle in the specified view’s coordinate system to a map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:torectto:))*