# init(lookingAt:forViewSize:allowPitch:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Returns a new camera object using the specified map item, view size, and pitch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
convenience init(lookingAt mapItem: MKMapItem, forViewSize viewSize: CGSize, allowPitch: Bool)
```

```objc
+ (instancetype) cameraLookingAtMapItem:(MKMapItem *) mapItem forViewSize:(CGSize) viewSize allowPitch:(BOOL) allowPitch;
```

## Parameters

- `mapItem`: An [`MKMapItem`](../mkmapitem.md) that indicates the location of the camera.
- `viewSize`: The view’s size.
- `allowPitch`: A Boolean value that indicates if the camera should the use map’s pitch angle.

## See Also

### Getting a camera object
- [convenience init(lookingAtCenter: CLLocationCoordinate2D, fromEyeCoordinate: CLLocationCoordinate2D, eyeAltitude: CLLocationDistance)](./init%28lookingatcenter,fromeyecoordinate,eyealtitude%29.md)
  Returns a new camera object using the specified viewing angle information.
- [convenience init(lookingAtCenter: CLLocationCoordinate2D, fromDistance: CLLocationDistance, pitch: CGFloat, heading: CLLocationDirection)](./init%28lookingatcenter,fromdistance,pitch,heading%29.md)
  Returns a new camera object using the specified distance, pitch, and heading information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamera/init(lookingat:forviewsize:allowpitch:))*