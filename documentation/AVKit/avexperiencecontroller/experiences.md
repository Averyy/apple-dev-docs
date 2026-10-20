# AVExperienceController.Experiences

**Framework**: AVKit  
**Kind**: struct  
**Role**: Structure

A structure that represents a collection of experiences to use with an experience controller.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@preconcurrency
struct Experiences
```

#### Overview

When creating, choose between using [`only(_:)`](./experiences/only%28_%29.md) or [`recommended(excluding:including:)`](./experiences/recommended%28excluding,including%29.md). Use [`only(_:)`](./experiences/only%28_%29.md) to specify the list of supported experiences. Use [`recommended(excluding:including:)`](./experiences/recommended%28excluding,including%29.md) to include the default set of experiences appropriate for a given platform.

Experiences can be explicitly included or excluded from this list with the corresponding parameters.

## Topics

### Defining experiences
- [static func only<C>(C) -> AVExperienceController.Experiences](./experiences/only%28_%29.md)
  Returns a set of experiences for the provided list.
- [static func recommended<C>(excluding: C, including: C) -> AVExperienceController.Experiences](./experiences/recommended%28excluding,including%29.md)
  Returns the recommended set of experiences.

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Configuring the experience
- [var allowedExperiences: AVExperienceController.Experiences](./allowedexperiences.md)
  The set of experiences the app supports.
- [var availableExperiences: AVExperienceController.Experiences](./availableexperiences.md)
  The allowed experiences that are available to use on the device at this time.
- [var experience: AVExperienceController.Experience](./experience-swift.property.md)
  The current experience.
- [AVExperienceController.Experience](./experience-swift.enum.md)
  The types of experiences the system supports.
- [var configuration: AVExperienceController.Configuration](./configuration-swift.property.md)
  The configuration options per experience.
- [AVExperienceController.Configuration](./configuration-swift.struct.md)
  Options that configure each experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experiences)*