# altitude

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Vertical distance, in meters, between this anchor and sea level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```objc
@property (nonatomic, readonly) CLLocationDistance altitude;
```

## Discussion

Negative values indicate below sea level. This property is valid only when [`altitudeSource`](./altitudesource-swift.property.md) is a value other than [`ARGeoAnchor.AltitudeSource.unknown`](./altitudesource-swift.enum/unknown.md).

## See Also

### Defining Altitude
- [var altitudeSource: ARGeoAnchor.AltitudeSource](./altitudesource-swift.property.md)
  A record of the source from which an altitude came.
- [ARGeoAnchor.AltitudeSource](./altitudesource-swift.enum.md)
  Options for setting a location anchor’s altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitude-9kges)*