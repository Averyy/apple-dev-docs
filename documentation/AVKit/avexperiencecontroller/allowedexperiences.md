# allowedExperiences

**Framework**: AVKit  
**Kind**: property

The set of experiences the application supports.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final var allowedExperiences: AVExperienceController.Experiences { get set }
```

#### Discussion

Use this to allow additional experiences like multiview, or to disable expanded. This list is the basis for [`availableExperiences`](avexperiencecontroller/availableexperiences.md), which filters out inapplicable experiences.

> **Note**: Because [`AVExperienceController.Experience.embedded`](avexperiencecontroller/experience-swift.enum/embedded.md) is the initial experience, and the one returned to when others end, it’s a programming error to exclude it from this list.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/allowedexperiences)*