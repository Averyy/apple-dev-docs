# ARGeoAnchor.AltitudeSource

**Framework**: ARKit  
**Kind**: enum

Options for setting a location anchor’s altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum AltitudeSource
```

#### Discussion

Each altitude source has unique performance and accuracy characteristics.

## Topics

### Sources
- [ARGeoAnchor.AltitudeSource.precise](argeoanchor/altitudesource-swift.enum/precise.md)
  The framework sets the altitude using a high-resolution digital-elevation model.
- [ARGeoAnchor.AltitudeSource.coarse](argeoanchor/altitudesource-swift.enum/coarse.md)
  The framework sets the altitude using a coarse digital-elevation model.
- [ARGeoAnchor.AltitudeSource.userDefined](argeoanchor/altitudesource-swift.enum/userdefined.md)
  The app defines the altitude.
- [ARGeoAnchor.AltitudeSource.unknown](argeoanchor/altitudesource-swift.enum/unknown.md)
  Altitude isn’t yet set.
### Initializers
- [init?(rawValue: Int)](argeoanchor/altitudesource-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var altitude: CLLocationDistance?](argeoanchor/altitude-89k4x.md)
  Vertical distance, in meters, between this anchor and sea level.
- [var altitudeSource: ARGeoAnchor.AltitudeSource](argeoanchor/altitudesource-swift.property.md)
  A record of the source from which an altitude came.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitudesource-swift.enum)*