# altitude

**Framework**: ARKit  
**Kind**: property

Vertical distance, in meters, between this anchor and sea level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
@nonobjc
var altitude: CLLocationDistance? { get }
```

#### Discussion

Negative values indicate below sea level. This property is valid only when [`altitudeSource`](argeoanchor/altitudesource-swift.property.md) is a value other than [`ARGeoAnchor.AltitudeSource.unknown`](argeoanchor/altitudesource-swift.enum/unknown.md).

## See Also

- [var altitudeSource: ARGeoAnchor.AltitudeSource](argeoanchor/altitudesource-swift.property.md)
  A record of the source from which an altitude came.
- [ARGeoAnchor.AltitudeSource](argeoanchor/altitudesource-swift.enum.md)
  Options for setting a location anchor’s altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitude-89k4x)*