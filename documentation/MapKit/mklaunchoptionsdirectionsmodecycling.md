# MKLaunchOptionsDirectionsModeCycling

**Framework**: MapKit  
**Kind**: var

Cycling directions between the specified start and end points.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let MKLaunchOptionsDirectionsModeCycling: String
```

#### Discussion

You can use this launch options key to open the Maps app directly in the mode that enables route planning that returns cycling directions, as shown in this example.

```swift
    Button("Cycling Directions") {
        selectedItem.openInMaps(
            launchOptions: [MKLaunchOptionsDirectionsModeKey: MKLaunchOptionsDirectionsModeCycling]
        )
    }
```

## See Also

- [let MKLaunchOptionsCameraKey: String](mklaunchoptionscamerakey.md)
  The virtual camera to use for viewing the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodecycling)*