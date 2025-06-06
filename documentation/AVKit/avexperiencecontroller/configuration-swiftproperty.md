# configuration

**Framework**: AVKit  
**Kind**: property

The configuration options per experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final var configuration: AVExperienceController.Configuration
```

#### Discussion

You may modify the configuration at any time, but after the [`experienceController(_:prepareForTransitionUsing:)`](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:).md) delegate callback returns, the system copies the configuration and uses it for the ensuing transition. Further modifications affect subsequent transitions.

## See Also

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
- [AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.struct.md)
  A structure that stores per-experience configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.property)*