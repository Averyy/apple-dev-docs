# MKLaunchOptionsCameraKey

**Framework**: MapKit  
**Kind**: var

The virtual camera to use for viewing the map.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let MKLaunchOptionsCameraKey: String
```

#### Discussion

The value of this key is an [`MKMapCamera`](mkmapcamera.md) object that describes a virtual camera that can specify a 3D perspective for the map. If you don’t specify this key, the Maps app uses its current settings to define the appearance of the map.

## See Also

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
- [let MKLaunchOptionsMapTypeKey: String](mklaunchoptionsmaptypekey.md)
  The type of map (standard, satellite, or hybrid) to display.
- [let MKLaunchOptionsShowsTrafficKey: String](mklaunchoptionsshowstraffickey.md)
  A Boolean value that indicates whether to display traffic information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklaunchoptionscamerakey)*