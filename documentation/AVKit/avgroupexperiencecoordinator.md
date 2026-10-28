# AVGroupExperienceCoordinator

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

An object that synchronizes viewing environment state across participants in a SharePlay session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@objc(AVGroupExperienceCoordinator)
class AVGroupExperienceCoordinator
```

## Overview

Access an experience coordinator by querying a player view controller for its [`groupExperienceCoordinator`](./avplayerviewcontroller/groupexperiencecoordinator.md) object.

## Topics

### Coordinating state changes
- [func coordinateWithSession<T>(GroupSession<T>)](./avgroupexperiencecoordinator/coordinatewithsession%28_%29.md)
  Begins coordinating viewing environment state with a group session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Immersive and multiview media
- [Playing immersive media with AVKit](./playing-immersive-media-with-avkit.md)
  Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](./creating-a-multiview-video-playback-experience-in-visionos.md)
  Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [class AVExperienceController](./avexperiencecontroller.md)
  An object that controls video experiences.
- [class AVMultiviewManager](./avmultiviewmanager.md)
  An object that manages viewing multiple videos at once.
- [class AVViewport](./avviewport.md)
  An object that provides configuration options for how the player displays content in different viewing contexts.
- [class AVPortalViewport](./avportalviewport.md)
  An object that defines the visual parameters for content displayed within a portal frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avgroupexperiencecoordinator)*