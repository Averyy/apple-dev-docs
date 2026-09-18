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
  The default multiview manager.
### Providing additional UI
- [var contentSelectionViewController: AVContentSelectionViewController?](avmultiviewmanager/contentselectionviewcontroller.md)
  A view controller that presents a user interface to select additional video content to display.
- [class AVContentSelectionViewController](avcontentselectionviewcontroller.md)
  A view controller for providing additional UI to the multiview experience.
### Dismissing the multiview experience
- [func dismiss()](avmultiviewmanager/dismiss.md)
  Dismisses the multiview presentation.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Playing immersive media with AVKit](playing-immersive-media-with-avkit.md)
  Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md)
  Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [class AVExperienceController](avexperiencecontroller.md)
  An object that controls video experiences.
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.
- [class AVViewport](avviewport.md)
  An object that provides configuration options for how the player displays content in different viewing contexts.
- [class AVPortalViewport](avportalviewport.md)
  An object that defines the visual parameters for content displayed within a portal frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avmultiviewmanager)*