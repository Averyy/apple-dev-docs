# MKStandardMapConfiguration

**Framework**: MapKit  
**Kind**: class

The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MKStandardMapConfiguration
```

## Topics

### Creating a standard map configuration
- [init()](mkstandardmapconfiguration/init.md)
  Creates a new standard map configuration.
- [convenience init(elevationStyle: MKMapConfiguration.ElevationStyle)](mkstandardmapconfiguration/init(elevationstyle:).md)
  Creates a new standard map configuration with the specified elevation style.
- [convenience init(elevationStyle: MKMapConfiguration.ElevationStyle, emphasisStyle: MKStandardMapConfiguration.EmphasisStyle)](mkstandardmapconfiguration/init(elevationstyle:emphasisstyle:).md)
  Creates a standard map configuration with the specified elevation and emphasis styles.
- [convenience init(emphasisStyle: MKStandardMapConfiguration.EmphasisStyle)](mkstandardmapconfiguration/init(emphasisstyle:).md)
  Creates a standard map configuration with the specified emphasis style.
- [MKMapConfiguration.ElevationStyle](mkmapconfiguration/elevationstyle-swift.enum.md)
  Values that control the map’s elevation style.
- [MKStandardMapConfiguration.EmphasisStyle](mkstandardmapconfiguration/emphasisstyle-swift.enum.md)
  Values that control how the framework emphasizes map features.
### Customizing the map display
- [var emphasisStyle: MKStandardMapConfiguration.EmphasisStyle](mkstandardmapconfiguration/emphasisstyle-swift.property.md)
  The value that indicates how the framework emphasizes map features.
- [MKStandardMapConfiguration.EmphasisStyle](mkstandardmapconfiguration/emphasisstyle-swift.enum.md)
  Values that control how the framework emphasizes map features.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkstandardmapconfiguration/pointofinterestfilter.md)
  The filter used to determine the points of interest shown on the map.
- [var showsTraffic: Bool](mkstandardmapconfiguration/showstraffic.md)
  A Boolean value that controls whether the map displays traffic conditions.

## Relationships

### Inherits From
- [MKMapConfiguration](mkmapconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var preferredConfiguration: MKMapConfiguration](mkmapview/preferredconfiguration.md)
  The characteristics of the map view, including the map type and features the map displays.
- [var pitchButtonVisibility: MKFeatureVisibility](mkmapview/pitchbuttonvisibility.md)
  A value that indicates whether the map’s pitch button is visible.
- [var showsUserTrackingButton: Bool](mkmapview/showsusertrackingbutton.md)
  A Boolean value that indicates whether the map displays the user tracking button.
- [class MKMapConfiguration](mkmapconfiguration.md)
  An abstract class that represents the shared elements of map configurations.
- [class MKHybridMapConfiguration](mkhybridmapconfiguration.md)
  The class that represents a satellite image of the area with road and road name information layers on top.
- [class MKImageryMapConfiguration](mkimagerymapconfiguration.md)
  The class that represents an imagery-based map presentation, such as one using satellite imagery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkstandardmapconfiguration)*