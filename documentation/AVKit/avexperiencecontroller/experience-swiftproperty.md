# experience

**Framework**: AVKit  
**Kind**: property

The current experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final var experience: AVExperienceController.Experience { get }
```

#### Discussion

The system updates this value only after the [`status`](avexperiencecontroller/transitioncontext/status-swift.property.md) changes to [`AVExperienceController.TransitionContext.Status.finished(result:)`](avexperiencecontroller/transitioncontext/status-swift.enum/finished(result:).md).

Implement the [`experienceController(_:didChangeTransitionContext:)`](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:).md) delegate method to observe changes to this value.

## See Also

- [var allowedExperiences: AVExperienceController.Experiences](avexperiencecontroller/allowedexperiences.md)
  The set of experiences the application supports.
- [var availableExperiences: AVExperienceController.Experiences](avexperiencecontroller/availableexperiences.md)
  The allowed experiences that are available to use on the device at this time.
- [AVExperienceController.Experiences](avexperiencecontroller/experiences.md)
  A structure that represents a collection of experiences to use with an experience controller.
- [AVExperienceController.Experience](avexperiencecontroller/experience-swift.enum.md)
  The types of experiences the system supports.
- [var configuration: AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.property.md)
  The configuration options per experience.
- [AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.struct.md)
  A structure that stores per-experience configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.property)*