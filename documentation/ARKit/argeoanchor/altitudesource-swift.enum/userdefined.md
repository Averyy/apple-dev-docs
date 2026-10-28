# ARGeoAnchor.AltitudeSource.userDefined

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

The app defines the altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case userDefined
```

```c
ARAltitudeSourceUserDefined
```

## Discussion

ARKit records this altitude source when your app defines a geo anchor’s altitude.

You may acquire altitude by providing a particular scene coordinate to the session using [`getGeoLocation(forPoint:completionHandler:)`](../../arsession/getgeolocation%28forpoint,completionhandler%29.md).

For example, your app might set a geo anchor’s altitude by raycasting a surface, then adding an arbitrary `y-`amount to make the anchor more visible from afar.

## See Also

### Sources
- [ARGeoAnchor.AltitudeSource.precise](./precise.md)
  The framework sets the altitude using a high-resolution digital-elevation model.
- [ARGeoAnchor.AltitudeSource.coarse](./coarse.md)
  The framework sets the altitude using a coarse digital-elevation model.
- [ARGeoAnchor.AltitudeSource.unknown](./unknown.md)
  Altitude isn’t yet set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitudesource-swift.enum/userdefined)*