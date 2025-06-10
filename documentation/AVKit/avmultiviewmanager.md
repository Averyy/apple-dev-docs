# AVMultiviewManager

**Framework**: AVKit  
**Kind**: class

An object that manages viewing multiple videos at once.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final class AVMultiviewManager
```

#### Overview

Watch multiple videos at the same time with [`AVExperienceController.Experience.multiview`](avexperiencecontroller/experience-swift.enum/multiview.md) using multiple [`AVExperienceController`](avexperiencecontroller.md) objects.

## Topics

### Accessing the default instance
- [static var `default`: AVMultiviewManager](avmultiviewmanager/default.md)
  Use this default AVMultiviewManager to customize the multiview experience.
### Providing additional UI
- [var contentSelectionViewController: AVContentSelectionViewController?](avmultiviewmanager/contentselectionviewcontroller.md)
  A view controller that presents a user interface to select additional video content to display.
- [class AVContentSelectionViewController](avcontentselectionviewcontroller.md)
  A view controller for providing additional UI to the multiview experience.
### Dismissing the multiview experience
- [func dismiss()](avmultiviewmanager/dismiss.md)
  Dismiss the multiview presentation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avmultiviewmanager)*