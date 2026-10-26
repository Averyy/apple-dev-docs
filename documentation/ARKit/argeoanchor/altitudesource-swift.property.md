# altitudeSource

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A record of the source from which an altitude came.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
var altitudeSource: ARGeoAnchor.AltitudeSource { get }
```

```objc
@property (nonatomic, readonly) ARAltitudeSource altitudeSource;
```

#### Discussion

The value of this property is [`ARGeoAnchor.AltitudeSource.userDefined`](./altitudesource-swift.enum/userdefined.md) if you set the altitude yourself (see [`getGeoLocation(forPoint:completionHandler:)`](../arsession/getgeolocation%28forpoint,completionhandler%29.md)).

If your app doesn’t set the altitude, ARKit populates this property to indicate the altitude’s expected accuracy (either [`ARGeoAnchor.AltitudeSource.precise`](./altitudesource-swift.enum/precise.md), or [`ARGeoAnchor.AltitudeSource.coarse`](./altitudesource-swift.enum/coarse.md)), depending on the level of confidence ARKit has with the altitude data that’s available at the time.

## See Also

### Defining Altitude
- [var altitude: CLLocationDistance?](./altitude-89k4x.md)
  Vertical distance, in meters, between this anchor and sea level.
- [ARGeoAnchor.AltitudeSource](./altitudesource-swift.enum.md)
  Options for setting a location anchor’s altitude.
- [altitude](./altitude-9kges.md)
  Vertical distance, in meters, between this anchor and sea level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitudesource-swift.property)*