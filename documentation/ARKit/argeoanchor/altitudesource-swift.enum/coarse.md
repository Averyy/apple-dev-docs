# ARGeoAnchor.AltitudeSource.coarse

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

The framework sets the altitude using a coarse digital-elevation model.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case coarse
```

```c
ARAltitudeSourceCoarse
```

## Discussion

The accuracy of this altitude is noticeably imprecise at close range, but it’s sufficient from far away. Use this option to save computational resources for anchors that are far off in the distance.

## See Also

### Sources
- [ARGeoAnchor.AltitudeSource.precise](./precise.md)
  The framework sets the altitude using a high-resolution digital-elevation model.
- [ARGeoAnchor.AltitudeSource.userDefined](./userdefined.md)
  The app defines the altitude.
- [ARGeoAnchor.AltitudeSource.unknown](./unknown.md)
  Altitude isn’t yet set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/altitudesource-swift.enum/coarse)*