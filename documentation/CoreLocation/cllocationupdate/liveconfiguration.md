# CLLocationUpdate.LiveConfiguration

**Framework**: Core Location  
**Kind**: enum  
**Role**: Enumeration

Values that indicate the kind of positioning updates the framework delivers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum LiveConfiguration
```

## Topics

### Location types
- [CLLocationUpdate.LiveConfiguration.default](./liveconfiguration/default.md)
  The value that configures positioning for activities that one of the other activity types doesn’t cover.
- [CLLocationUpdate.LiveConfiguration.airborne](./liveconfiguration/airborne.md)
  The value that configures positioning for activities in the air.
- [CLLocationUpdate.LiveConfiguration.automotiveNavigation](./liveconfiguration/automotivenavigation.md)
  The value that configures positioning for an automobile following a road network.
- [CLLocationUpdate.LiveConfiguration.fitness](./liveconfiguration/fitness.md)
  The value that configures positioning for dedicated fitness sessions.
- [CLLocationUpdate.LiveConfiguration.maritime](./liveconfiguration/maritime.md)
  The value that configures positioning for vessels on water, including while anchored.
- [CLLocationUpdate.LiveConfiguration.otherNavigation](./liveconfiguration/othernavigation.md)
  The value that configures positioning for transportation that doesn’t, or may not, adhere to roads, such as cycling, scooters, trains, boats, and off-road vehicles.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Receiving location updates
- [static func liveUpdates(CLLocationUpdate.LiveConfiguration) -> CLLocationUpdate.Updates](./liveupdates%28_%29.md)
  Tells Core Location to start delivering the location updates it produces for the configuration you specify.
- [CLLocationUpdate.Updates](./updates.md)
  A structure that represents an asynchronous sequence of location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationupdate/liveconfiguration)*