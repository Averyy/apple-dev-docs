# AVExperienceController.Experience

**Framework**: AVKit  
**Kind**: enum

The types of experiences the system supports.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum Experience
```

## Topics

### Supported experiences
- [AVExperienceController.Experience.embedded](avexperiencecontroller/experience-swift.enum/embedded.md)
  An experience where the video embeds within its original container.
- [AVExperienceController.Experience.expanded](avexperiencecontroller/experience-swift.enum/expanded.md)
  An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.multiview](avexperiencecontroller/experience-swift.enum/multiview.md)
  An experience where multiple videos play together.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var allowedExperiences: AVExperienceController.Experiences](avexperiencecontroller/allowedexperiences.md)
  The set of experiences the application supports.
- [var availableExperiences: AVExperienceController.Experiences](avexperiencecontroller/availableexperiences.md)
  The allowed experiences that are available to use on the device at this time.
- [AVExperienceController.Experiences](avexperiencecontroller/experiences.md)
  A structure that represents a collection of experiences to use with an experience controller.
- [var experience: AVExperienceController.Experience](avexperiencecontroller/experience-swift.property.md)
  The current experience.
- [var configuration: AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.property.md)
  The configuration options per experience.
- [AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.struct.md)
  A structure that stores per-experience configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum)*