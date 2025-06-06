# availableExperiences

**Framework**: AVKit  
**Kind**: property

The allowed experiences that are available to use on the device at this time.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final var availableExperiences: AVExperienceController.Experiences { get }
```

#### Discussion

This property is a subset of [`allowedExperiences`](avexperiencecontroller/allowedexperiences.md), filtered for platform, device configuration, and system state.

## See Also

- [var allowedExperiences: AVExperienceController.Experiences](avexperiencecontroller/allowedexperiences.md)
  The set of experiences the application supports.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/availableexperiences)*