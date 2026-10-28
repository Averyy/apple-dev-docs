# camera

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Returns a new camera object for you to configure.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (instancetype) camera;
```

## Return Value

A new camera object.

## Discussion

You must change the values of the returned camera object before using it.

## See Also

### Getting a camera object
- [convenience init(lookingAtCenter: CLLocationCoordinate2D, fromEyeCoordinate: CLLocationCoordinate2D, eyeAltitude: CLLocationDistance)](./init%28lookingatcenter,fromeyecoordinate,eyealtitude%29.md)
  Returns a new camera object using the specified viewing angle information.
- [convenience init(lookingAtCenter: CLLocationCoordinate2D, fromDistance: CLLocationDistance, pitch: CGFloat, heading: CLLocationDirection)](./init%28lookingatcenter,fromdistance,pitch,heading%29.md)
  Returns a new camera object using the specified distance, pitch, and heading information.
- [convenience init(lookingAt: MKMapItem, forViewSize: CGSize, allowPitch: Bool)](./init%28lookingat,forviewsize,allowpitch%29.md)
  Returns a new camera object using the specified map item, view size, and pitch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamera/camera)*