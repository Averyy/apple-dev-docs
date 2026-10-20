# ARGeoAnchor.AltitudeSource

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Options for setting a location anchor’s altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
enum AltitudeSource
```

```c
enum ARAltitudeSource : NSInteger;
```

#### Discussion

Each altitude source has unique performance and accuracy characteristics.

## Topics

### Sources
- [ARGeoAnchor.AltitudeSource.precise](./altitudesource-swift.enum/precise.md)
  The framework sets the altitude using a high-resolution digital-elevation model.
- [ARGeoAnchor.AltitudeSource.coarse](./altitudesource-swift.enum/coarse.md)
  The framework sets the altitude using a coarse digital-elevation model.
- [ARGeoAnchor.AltitudeSource.userDefined](./altitudesource-swift.enum/userdefined.md)
  The app defines the altitude.
- [ARGeoAnchor.AltitudeSource.unknown](./altitudesource-swift.enum/unknown.md)
  Altitude isn’t yet set.
### Initializers
- [init?(rawValue: Int)](./altitudesource-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining Altitude
- [var altitude: CLLocationDistance?](./altitude-89k4x.md)
  Vertical distance, in meters, between this anchor and sea level.
- [var altitudeSource: ARGeoAnchor.AltitudeSource](./altitudesource-swift.property.md)
  A record of the source from which an altitude came.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitudesource-swift.enum)*