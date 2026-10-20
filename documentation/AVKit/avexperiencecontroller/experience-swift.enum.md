# AVExperienceController.Experience

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

The types of experiences the system supports.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@preconcurrency
enum Experience
```

## Topics

### Supported experiences
- [AVExperienceController.Experience.embedded](./experience-swift.enum/embedded.md)
  An experience where the video embeds within its original container.
- [AVExperienceController.Experience.expanded](./experience-swift.enum/expanded.md)
  An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.multiview](./experience-swift.enum/multiview.md)
  An experience where multiple videos play together.
- [AVExperienceController.Experience.immersive](./experience-swift.enum/immersive.md)
  Indicates an experience in which the video extends beyond the app window boundaries/container.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the experience
- [var allowedExperiences: AVExperienceController.Experiences](./allowedexperiences.md)
  The set of experiences the app supports.
- [var availableExperiences: AVExperienceController.Experiences](./availableexperiences.md)
  The allowed experiences that are available to use on the device at this time.
- [AVExperienceController.Experiences](./experiences.md)
  A structure that represents a collection of experiences to use with an experience controller.
- [var experience: AVExperienceController.Experience](./experience-swift.property.md)
  The current experience.
- [var configuration: AVExperienceController.Configuration](./configuration-swift.property.md)
  The configuration options per experience.
- [AVExperienceController.Configuration](./configuration-swift.struct.md)
  Options that configure each experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum)*