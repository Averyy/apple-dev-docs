# AVExperienceController.Configuration

**Framework**: AVKit  
**Kind**: struct

Options that configure each experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Configuring experiences
- [var expanded: AVExperienceController.ExpandedConfiguration](avexperiencecontroller/configuration-swift.struct/expanded.md)
  Configuration options for an expanded experience.
- [AVExperienceController.ExpandedConfiguration](avexperiencecontroller/expandedconfiguration.md)
  A structure that specifies options for an expanded experience.
### Configuring placement
- [var placement: AVExperienceController.Configuration.Placement](avexperiencecontroller/configuration-swift.struct/placement-swift.property.md)
  Supply a Placement to be used when the original container isn’t added to the view controller hierarchy; i.e. the AVPlayerViewController is off-screen.
- [AVExperienceController.Configuration.Placement](avexperiencecontroller/configuration-swift.struct/placement-swift.struct.md)
  A struct used to set the placement for the media playback to be experienced.

## See Also

- [var allowedExperiences: AVExperienceController.Experiences](avexperiencecontroller/allowedexperiences.md)
  The set of experiences the app supports.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.struct)*