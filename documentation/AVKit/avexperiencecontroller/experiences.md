# AVExperienceController.Experiences

**Framework**: AVKit  
**Kind**: struct

A structure that represents a collection of experiences to use with an experience controller.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Experiences
```

#### Overview

When creating, choose between using [`only(_:)`](avexperiencecontroller/experiences/only(_:).md) or [`recommended(excluding:including:)`](avexperiencecontroller/experiences/recommended(excluding:including:).md). Use [`only(_:)`](avexperiencecontroller/experiences/only(_:).md) to specify the list of supported experiences. Use [`recommended(excluding:including:)`](avexperiencecontroller/experiences/recommended(excluding:including:).md) to include the default set of experiences appropriate for a given platform.

Experiences can be explicitly included or excluded from this list with the corresponding parameters.

## Topics

### Defining experiences
- [static func only<C>(C) -> AVExperienceController.Experiences](avexperiencecontroller/experiences/only(_:).md)
  Returns a set of experiences for the provided list.
- [static func recommended<C>(excluding: C, including: C) -> AVExperienceController.Experiences](avexperiencecontroller/experiences/recommended(excluding:including:).md)
  Returns the recommended set of experiences.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var allowedExperiences: AVExperienceController.Experiences](avexperiencecontroller/allowedexperiences.md)
  The set of experiences the application supports.
- [var availableExperiences: AVExperienceController.Experiences](avexperiencecontroller/availableexperiences.md)
  The allowed experiences that are available to use on the device at this time.
- [var experience: AVExperienceController.Experience](avexperiencecontroller/experience-swift.property.md)
  The current experience.
- [AVExperienceController.Experience](avexperiencecontroller/experience-swift.enum.md)
  The types of experiences the system supports.
- [var configuration: AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.property.md)
  The configuration options per experience.
- [AVExperienceController.Configuration](avexperiencecontroller/configuration-swift.struct.md)
  A structure that stores per-experience configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experiences)*