# ARGeoAnchor.AltitudeSource.userDefined

**Framework**: ARKit  
**Kind**: case

The app defines the altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case userDefined
```

#### Discussion

ARKit records this altitude source when your app defines a geo anchor’s altitude.

You may acquire altitude by providing a particular scene coordinate to the session using [`getGeoLocation(forPoint:completionHandler:)`](arsession/getgeolocation(forpoint:completionhandler:).md).

For example, your app might set a geo anchor’s altitude by raycasting a surface, then adding an arbitrary `y-`amount to make the anchor more visible from afar.

## See Also

- [ARGeoAnchor.AltitudeSource.precise](argeoanchor/altitudesource-swift.enum/precise.md)
  The framework sets the altitude using a high-resolution digital-elevation model.
- [ARGeoAnchor.AltitudeSource.coarse](argeoanchor/altitudesource-swift.enum/coarse.md)
  The framework sets the altitude using a coarse digital-elevation model.
- [ARGeoAnchor.AltitudeSource.unknown](argeoanchor/altitudesource-swift.enum/unknown.md)
  Altitude isn’t yet set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitudesource-swift.enum/userdefined)*