# MKUserTrackingMode

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

The mode to use for tracking the user’s location on the map.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
enum MKUserTrackingMode
```

```c
enum MKUserTrackingMode : NSInteger;
```

## Topics

### Constants
- [MKUserTrackingMode.none](./mkusertrackingmode/none.md)
  The map doesn’t follow the user’s location.
- [MKUserTrackingMode.follow](./mkusertrackingmode/follow.md)
  The map follows the user location.
- [MKUserTrackingMode.followWithHeading](./mkusertrackingmode/followwithheading.md)
  The map follows the user’s location and rotates when the heading changes.
### Initializers
- [init?(rawValue: Int)](./mkusertrackingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Displaying the user’s location
- [Converting a user’s location to a descriptive placemark](./converting-a-user-s-location-to-a-descriptive-placemark.md)
  Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [var showsUserLocation: Bool](./mkmapview/showsuserlocation.md)
  A Boolean value that indicates whether the map tries to display the user’s location.
- [var isUserLocationVisible: Bool](./mkmapview/isuserlocationvisible.md)
  A Boolean value that indicates whether the user’s location is visible in the map view.
- [var userLocation: MKUserLocation](./mkmapview/userlocation.md)
  The annotation object that represents the user’s location.
- [var userTrackingMode: MKUserTrackingMode](./mkmapview/usertrackingmode.md)
  The mode to use for tracking the user’s location.
- [func setUserTrackingMode(MKUserTrackingMode, animated: Bool)](./mkmapview/setusertrackingmode%28_,animated%29.md)
  Sets the mode to use for tracking the user’s location, with optional animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkusertrackingmode)*