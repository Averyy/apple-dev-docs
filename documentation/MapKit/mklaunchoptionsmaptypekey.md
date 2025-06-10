# MKLaunchOptionsMapTypeKey

**Framework**: MapKit  
**Kind**: var

The type of map (standard, satellite, or hybrid) to display.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
let MKLaunchOptionsMapTypeKey: String
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object whose value is an integer corresponding to an [`MKMapType`](mkmaptype.md) value.

## See Also

- [let MKLaunchOptionsCameraKey: String](mklaunchoptionscamerakey.md)
  The virtual camera to use for viewing the map.
- [let MKLaunchOptionsDirectionsModeCycling: String](mklaunchoptionsdirectionsmodecycling.md)
  Cycling directions between the specified start and end points.
- [let MKLaunchOptionsDirectionsModeDefault: String](mklaunchoptionsdirectionsmodedefault.md)
  Directions that match the user’s preferred transportation type.
- [let MKLaunchOptionsDirectionsModeDriving: String](mklaunchoptionsdirectionsmodedriving.md)
  Driving directions between the specified start and end points.
- [let MKLaunchOptionsDirectionsModeKey: String](mklaunchoptionsdirectionsmodekey.md)
  The mode of transportation.
- [let MKLaunchOptionsDirectionsModeTransit: String](mklaunchoptionsdirectionsmodetransit.md)
  Public transit directions between the specified start and end points.
- [let MKLaunchOptionsDirectionsModeWalking: String](mklaunchoptionsdirectionsmodewalking.md)
  Walking directions between the specified start and end points.
- [let MKLaunchOptionsMapCenterKey: String](mklaunchoptionsmapcenterkey.md)
  The coordinate value on which to center the map.
- [let MKLaunchOptionsMapSpanKey: String](mklaunchoptionsmapspankey.md)
  The amount of the map to display.
- [let MKLaunchOptionsShowsTrafficKey: String](mklaunchoptionsshowstraffickey.md)
  A Boolean value that indicates whether to display traffic information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklaunchoptionsmaptypekey)*