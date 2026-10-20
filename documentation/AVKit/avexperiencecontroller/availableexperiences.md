# availableExperiences

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The allowed experiences that are available to use on the device at this time.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final var availableExperiences: AVExperienceController.Experiences { get }
```

#### Discussion

This property is a subset of [`allowedExperiences`](./allowedexperiences.md), filtered for platform, device configuration, and system state.

## See Also

### Configuring the experience
- [var allowedExperiences: AVExperienceController.Experiences](./allowedexperiences.md)
  The set of experiences the app supports.
- [AVExperienceController.Experiences](./experiences.md)
  A structure that represents a collection of experiences to use with an experience controller.
- [var experience: AVExperienceController.Experience](./experience-swift.property.md)
  The current experience.
- [AVExperienceController.Experience](./experience-swift.enum.md)
  The types of experiences the system supports.
- [var configuration: AVExperienceController.Configuration](./configuration-swift.property.md)
  The configuration options per experience.
- [AVExperienceController.Configuration](./configuration-swift.struct.md)
  Options that configure each experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/availableexperiences)*