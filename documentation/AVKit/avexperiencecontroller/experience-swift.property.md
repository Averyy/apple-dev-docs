# experience

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The current experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final var experience: AVExperienceController.Experience { get }
```

## Discussion

The system updates this value only after the [`status`](./transitioncontext/status-swift.property.md) changes to [`AVExperienceController.TransitionContext.Status.finished(result:)`](./transitioncontext/status-swift.enum/finished%28result%29.md).

Implement the [`experienceController(_:didChangeTransitionContext:)`](./delegate-swift.protocol/experiencecontroller%28_,didchangetransitioncontext%29.md) delegate method to observe changes to this value.

## See Also

### Configuring the experience
- [var allowedExperiences: AVExperienceController.Experiences](./allowedexperiences.md)
  The set of experiences the app supports.
- [var availableExperiences: AVExperienceController.Experiences](./availableexperiences.md)
  The allowed experiences that are available to use on the device at this time.
- [AVExperienceController.Experiences](./experiences.md)
  A structure that represents a collection of experiences to use with an experience controller.
- [AVExperienceController.Experience](./experience-swift.enum.md)
  The types of experiences the system supports.
- [var configuration: AVExperienceController.Configuration](./configuration-swift.property.md)
  The configuration options per experience.
- [AVExperienceController.Configuration](./configuration-swift.struct.md)
  Options that configure each experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.property)*