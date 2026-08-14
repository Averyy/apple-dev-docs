# AVPortalViewport

**Framework**: AVKit  
**Kind**: class

Defines the visual parameters for content displayed within a portal frame. Use this configuration to create cinematic viewing experiences with custom framing.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AVPortalViewport
```

#### Overview

Portal viewports allow you to control how immersive content is framed and presented to users. You can specify the aspect ratio of the portal frame to achieve the desired visual effect.

When properties are not explicitly set, the system provides sensible defaults:

- Aspect Ratio: Defaults to 16:9 (1.78) for standard widescreen content

> **Note**: Spatial videos do not support portal viewport settings.

```swift
let portalViewport = AVPortalViewport()
portalViewport.aspectRatio = 2.39
playerViewController.viewport.portal = portalViewport
```

## Topics

### Configuring the aspect ratio
- [var aspectRatio: Double?](avportalviewport/aspectratio-4drnq.md)
  The aspect ratio of the portal frame.

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
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.
- [class AVViewport](avviewport.md)
  Provides configuration options for how content is displayed in different viewing contexts. Use this object to customize the visual presentation of your content.
- [Third-party casting support](third-party-casting-support.md)
  Provide custom playback controls for third-party casting services and other media sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avportalviewport)*