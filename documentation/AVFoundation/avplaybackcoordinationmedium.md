# AVPlaybackCoordinationMedium

**Framework**: AVFoundation  
**Kind**: class

The AVPlaybackCoordinationMedium passes states and messages between its connected playback coordinators.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class AVPlaybackCoordinationMedium
```

#### Overview

The coordination medium passes states and messages from one playback coordinator to all other connected playback coordinators to enable coordination of rate changes and seeks. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Creating a coordination medium
- [init()](avplaybackcoordinationmedium/init.md)
  Initializes an AVPlaybackCoordinationMedium
### Managing playback coordinators
- [var connectedPlaybackCoordinators: [AVPlayerPlaybackCoordinator]](avplaybackcoordinationmedium/connectedplaybackcoordinators.md)
  All playback coordinators that are connected to the coordination medium.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Destination Video](../visionOS/destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Supporting coordinated media playback](supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [class AVPlaybackCoordinator](avplaybackcoordinator.md)
  An object that coordinates the playback of players in a connected group.
- [class AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md)
  A playback coordinator subclass that coordinates the playback of player objects in a connected group.
- [class AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md)
  A playback coordinator subclass that coordinates the playback of custom player objects in a connected group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinationmedium)*