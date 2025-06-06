# pitchButtonVisibility

**Framework**: MapKit  
**Kind**: property

A value that indicates whether the map’s pitch button is visible.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var pitchButtonVisibility: MKFeatureVisibility { get set }
```

#### Discussion

Use this button to display or hide a button that allows a person to set the map to a pleasing pitch or return the map to a flat appearance.

## See Also

- [var preferredConfiguration: MKMapConfiguration](mkmapview/preferredconfiguration.md)
  The characteristics of the map view, including the map type and features the map displays.
- [var showsUserTrackingButton: Bool](mkmapview/showsusertrackingbutton.md)
  A Boolean value that indicates whether the map displays the user tracking button.
- [class MKMapConfiguration](mkmapconfiguration.md)
  An abstract class that represents the shared elements of map configurations.
- [class MKStandardMapConfiguration](mkstandardmapconfiguration.md)
  The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [class MKHybridMapConfiguration](mkhybridmapconfiguration.md)
  The class that represents a satellite image of the area with road and road name information layers on top.
- [class MKImageryMapConfiguration](mkimagerymapconfiguration.md)
  The class that represents an imagery-based map presentation, such as one using satellite imagery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/pitchbuttonvisibility)*