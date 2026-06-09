# AVViewport

**Framework**: AVKit  
**Kind**: class

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AVViewport
```

#### Overview

A configuration object that manages viewport settings for different presentation modes.

AVViewport provides configuration options for how immersive content is displayed in different viewing contexts. Use this object to customize the visual presentation of your content within the visionOS environment.

```None
		The viewport configuration allows you to specify how content should be framed
		and presented to users. Currently, portal-based presentation is supported through
		the portal property.
```

## Topics

### Configuring the portal viewport
- [var portal: AVPortalViewport?](avviewport/portal.md)
- [class AVPortalViewport](avportalviewport.md)

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
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.
- [class AVPortalViewport](avportalviewport.md)
- [Third-party casting support](third-party-casting-support.md)
  Provide custom playback controls for third-party casting services and other media sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avviewport)*