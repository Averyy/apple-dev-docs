# MKMapConfiguration

**Framework**: MapKit  
**Kind**: class

An abstract class that represents the shared elements of map configurations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MKMapConfiguration
```

## Topics

### Controlling the elevation style
- [var elevationStyle: MKMapConfiguration.ElevationStyle](mkmapconfiguration/elevationstyle-swift.property.md)
  The value that indicates the map’s elevation style.
- [MKMapConfiguration.ElevationStyle](mkmapconfiguration/elevationstyle-swift.enum.md)
  Values that control the map’s elevation style.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MKHybridMapConfiguration](mkhybridmapconfiguration.md)
- [MKImageryMapConfiguration](mkimagerymapconfiguration.md)
- [MKStandardMapConfiguration](mkstandardmapconfiguration.md)
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
- [class MKStandardMapConfiguration](mkstandardmapconfiguration.md)
  The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [class MKHybridMapConfiguration](mkhybridmapconfiguration.md)
  The class that represents a satellite image of the area with road and road name information layers on top.
- [class MKImageryMapConfiguration](mkimagerymapconfiguration.md)
  The class that represents an imagery-based map presentation, such as one using satellite imagery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapconfiguration)*