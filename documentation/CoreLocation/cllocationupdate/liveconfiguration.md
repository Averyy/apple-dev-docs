# CLLocationUpdate.LiveConfiguration

**Framework**: Core Location  
**Kind**: enum

Values for indicating the kind of updates the framework delivers.

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
- [CLLocationUpdate.LiveConfiguration.default](cllocationupdate/liveconfiguration/default.md)
  The value that configures positioning for activities that one of the other activity types doesn’t cover.
- [CLLocationUpdate.LiveConfiguration.airborne](cllocationupdate/liveconfiguration/airborne.md)
  The value that configures positioning for activities in the air.
- [CLLocationUpdate.LiveConfiguration.automotiveNavigation](cllocationupdate/liveconfiguration/automotivenavigation.md)
  The value that configures positioning for an automobile following a road network.
- [CLLocationUpdate.LiveConfiguration.fitness](cllocationupdate/liveconfiguration/fitness.md)
  The value that configures positioning for dedicated fitness sessions.
- [CLLocationUpdate.LiveConfiguration.otherNavigation](cllocationupdate/liveconfiguration/othernavigation.md)
  The value that configures positioning for transportation that doesn’t, or may not, adhere to roads, such as cycling, scooters, trains, boats, and off-road vehicles.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [static func liveUpdates(CLLocationUpdate.LiveConfiguration) -> CLLocationUpdate.Updates](cllocationupdate/liveupdates(_:).md)
  Tells Core Location to start delivering the location updates it produces for the configuration you specify.
- [CLLocationUpdate.Updates](cllocationupdate/updates.md)
  A structure that represents an asynchronous sequence of location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationupdate/liveconfiguration)*