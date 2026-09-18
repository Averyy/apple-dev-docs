# AVViewport

**Framework**: AVKit  
**Kind**: class

An object that provides configuration options for how the player displays content in different viewing contexts.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
class AVViewport
```

#### Overview

Use this object to customize the visual presentation of your content, as the following example shows:

```swift
let portalViewport = AVPortalViewport()
portalViewport.aspectRatio = 2.39
playerViewController.viewport.portal = portalViewport
```

## Topics

### Configuring the portal viewport
- [var portal: AVPortalViewport?](avviewport/portal.md)
  The viewport configuration to use when the player displays immersive content in a portal.
- [class AVPortalViewport](avportalviewport.md)
  An object that defines the visual parameters for content displayed within a portal frame.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Playing immersive media with AVKit](playing-immersive-media-with-avkit.md)
  Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md)
  Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [class AVExperienceController](avexperiencecontroller.md)
  An object that controls video experiences.
- [class AVMultiviewManager](avmultiviewmanager.md)
  An object that manages viewing multiple videos at once.
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.
- [class AVPortalViewport](avportalviewport.md)
  An object that defines the visual parameters for content displayed within a portal frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avviewport)*