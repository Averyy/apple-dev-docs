# configuration

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The configuration options per experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
final var configuration: AVExperienceController.Configuration
```

## Discussion

You may modify the configuration at any time, but after the [`experienceController(_:prepareForTransitionUsing:)`](./delegate-swift.protocol/experiencecontroller%28_,preparefortransitionusing%29.md) delegate callback returns, the system copies the configuration and uses it for the ensuing transition. Further modifications affect subsequent transitions.

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
- [AVExperienceController.Experience](./experience-swift.enum.md)
  The types of experiences the system supports.
- [AVExperienceController.Configuration](./configuration-swift.struct.md)
  Options that configure each experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.property)*