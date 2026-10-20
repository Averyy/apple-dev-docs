# MKHybridMapConfiguration

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

The class that represents a satellite image of the area with road and road name information layers on top.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MKHybridMapConfiguration
```

```objc
@interface MKHybridMapConfiguration : MKMapConfiguration
```

## Topics

### Creating a hybrid map configuration
- [init()](./mkhybridmapconfiguration/init%28%29.md)
  Creates a new hybrid map configuration.
- [convenience init(elevationStyle: MKMapConfiguration.ElevationStyle)](./mkhybridmapconfiguration/init%28elevationstyle%29.md)
  Creates a new hybrid map configuration with the specified elevation style.
- [MKMapConfiguration.ElevationStyle](./mkmapconfiguration/elevationstyle-swift.enum.md)
  Values that control the map’s elevation style.
### Controlling what the map displays
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./mkhybridmapconfiguration/pointofinterestfilter.md)
  The filter the framework uses to determine the points of interest to show on the map.
- [var showsTraffic: Bool](./mkhybridmapconfiguration/showstraffic.md)
  A Boolean value that indicates whether the maps shows traffic conditions.

## Relationships

### Inherits From
- [MKMapConfiguration](./mkmapconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Configuring the map appearance
- [var preferredConfiguration: MKMapConfiguration](./mkmapview/preferredconfiguration.md)
  The characteristics of the map view, including the map type and features the map displays.
- [var pitchButtonVisibility: MKFeatureVisibility](./mkmapview/pitchbuttonvisibility.md)
  A value that indicates whether the map’s pitch button is visible.
- [var showsUserTrackingButton: Bool](./mkmapview/showsusertrackingbutton.md)
  A Boolean value that indicates whether the map displays the user tracking button.
- [class MKMapConfiguration](./mkmapconfiguration.md)
  An abstract class that represents the shared elements of map configurations.
- [class MKStandardMapConfiguration](./mkstandardmapconfiguration.md)
  The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [class MKImageryMapConfiguration](./mkimagerymapconfiguration.md)
  The class that represents an imagery-based map presentation, such as one using satellite imagery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkhybridmapconfiguration)*