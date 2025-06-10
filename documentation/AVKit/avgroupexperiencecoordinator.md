# AVGroupExperienceCoordinator

**Framework**: AVKit  
**Kind**: class

An object that synchronizes viewing environment state across participants in a SharePlay session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@objc
(AVGroupExperienceCoordinator) class AVGroupExperienceCoordinator
```

#### Overview

Access an experience coordinator by querying a player view controller for its [`groupExperienceCoordinator`](avplayerviewcontroller/groupexperiencecoordinator.md) object.

## Topics

### Coordinating state changes
- [func coordinateWithSession<T>(GroupSession<T>)](avgroupexperiencecoordinator/coordinatewithsession(_:).md)
  Begins coordinating viewing environment state with a group session.

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

## See Also

- [Playing immersive media with AVKit](playing-immersive-media-with-avkit.md)
  Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md)
  Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md)
  Provide an optimized viewing experience for watching 3D video content.
- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md)
  Display standard controls in your app to edit the timeline of the currently playing media.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVExperienceController](avexperiencecontroller.md)
  An object that controls video experiences.
- [class AVMultiviewManager](avmultiviewmanager.md)
  An object that manages viewing multiple videos at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avgroupexperiencecoordinator)*