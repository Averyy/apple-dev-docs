# altitudeSource

**Framework**: ARKit  
**Kind**: property

A record of the source from which an altitude came.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var altitudeSource: ARGeoAnchor.AltitudeSource { get }
```

#### Discussion

The value of this property is [`ARGeoAnchor.AltitudeSource.userDefined`](argeoanchor/altitudesource-swift.enum/userdefined.md) if you set the altitude yourself (see [`getGeoLocation(forPoint:completionHandler:)`](arsession/getgeolocation(forpoint:completionhandler:).md)).

If your app doesn’t set the altitude, ARKit populates this property to indicate the altitude’s expected accuracy (either [`ARGeoAnchor.AltitudeSource.precise`](argeoanchor/altitudesource-swift.enum/precise.md), or [`ARGeoAnchor.AltitudeSource.coarse`](argeoanchor/altitudesource-swift.enum/coarse.md)), depending on the level of confidence ARKit has with the altitude data that’s available at the time.

## See Also

- [var altitude: CLLocationDistance?](argeoanchor/altitude-89k4x.md)
  Vertical distance, in meters, between this anchor and sea level.
- [ARGeoAnchor.AltitudeSource](argeoanchor/altitudesource-swift.enum.md)
  Options for setting a location anchor’s altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitudesource-swift.property)*