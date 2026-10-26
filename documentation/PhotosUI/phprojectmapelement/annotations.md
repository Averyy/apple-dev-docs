# annotations

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An array of optional annotations attached to the map.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var annotations: [any MKAnnotation] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<id<MKAnnotation>> * annotations;
```

## See Also

### Pinpointing the Map
- [var mapType: MKMapType](./maptype.md)
  The type of map in the project.
- [var centerCoordinate: CLLocationCoordinate2D](./centercoordinate.md)
  The coordinates of the center of the map.
- [var heading: CLLocationDirection](./heading.md)
  The heading of the map.
- [var pitch: CGFloat](./pitch.md)
  The pitch of the map.
- [var altitude: CLLocationDistance](./altitude.md)
  The altitude of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectmapelement/annotations)*