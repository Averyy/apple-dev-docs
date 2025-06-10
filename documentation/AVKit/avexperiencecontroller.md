# AVExperienceController

**Framework**: AVKit  
**Kind**: class

An object that controls video experiences.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final class AVExperienceController
```

#### Overview

Use this class to control, observe, and respond to experience changes for an [`AVPlayerViewController`](avplayerviewcontroller.md). A player view controller’s presentation APIs will no longer be honored after attaching an experience controller. Using the other presentation APIs may preclude the use of this class.

## Topics

### Configuring the experience
- [var allowedExperiences: AVExperienceController.Experiences](avexperiencecontroller/allowedexperiences.md)
  The set of experiences the application supports.
- [var availableExperiences: AVExperienceController.Experiences](avexperiencecontroller/availableexperiences.md)
  The allowed experiences that are available to use on the device at this time.
- [AVExperienceController.Experiences](avexperiencecontroller/experiences.md)
  A structure that represents a collection of experiences to use with an experience controller.
- [var experience: AVExperienceController.Experience](avexperiencecontroller/experience-swift.property.md)
  The current experience.
- [AVExperienceController.Experience](avexperiencecontroller/experience-swift.enum.md)
  The types of experiences the system supports.
- [var configuration: AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.property.md)
  The configuration options per experience.
- [AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.struct.md)
  A structure that stores per-experience configuration.
### Transitioning experiences
- [func transition(to: AVExperienceController.Experience) async -> AVExperienceController.TransitionContext.TransitionResult](avexperiencecontroller/transition(to:).md)
  Transitions the video to a different experience.
### Configuring a delegate
- [var delegate: (any AVExperienceController.Delegate)?](avexperiencecontroller/delegate-swift.property.md)
  A delegate object for the experience controller.
- [AVExperienceController.Delegate](avexperiencecontroller/delegate-swift.protocol.md)
  A protocol that defines the methods to implement to respond to experience changes.
### Structures
- [AVExperienceController.ExpandedConfiguration](avexperiencecontroller/expandedconfiguration.md)
  A structure that specifies options for an expanded experience.
- [AVExperienceController.TransitionContext](avexperiencecontroller/transitioncontext.md)
  The state of the transition provided to the delegate object.

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
- [class AVMultiviewManager](avmultiviewmanager.md)
  An object that manages viewing multiple videos at once.
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller)*