# ImagePlaygroundOptions.Personalization

**Framework**: Image Playground  
**Kind**: enum

Options for enabling and disabling personalization features when generating images.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
enum Personalization
```

#### Overview

The SwiftUI sheets, [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) type, and [`ImageCreator`](imagecreator.md) type offer ways to personalize the images you create using an existing photo or other information. When configuring one of those types, create an instance of [`ImagePlaygroundOptions`](imageplaygroundoptions.md) and configure its [`personalization`](imageplaygroundoptions/personalization-swift.property.md) property with your personalization preferences.

Personalization tells the system how to craft the appearance of people in the images it creates. The system can derive appearance choices for people from additional sources, such as from photos in the person’s Photos library. If you disable personalization, the system uses only the prompts and starting image you provide to generate the images.

## Topics

### Enumeration Cases
- [ImagePlaygroundOptions.Personalization.automatic](imageplaygroundoptions/personalization-swift.enum/automatic.md)
  An option to choose the most appropriate personalization behavior.
- [ImagePlaygroundOptions.Personalization.disabled](imageplaygroundoptions/personalization-swift.enum/disabled.md)
  An option to disable personalization features during image generation.
- [ImagePlaygroundOptions.Personalization.enabled](imageplaygroundoptions/personalization-swift.enum/enabled.md)
  An option to enable personalization features during image generation.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/personalization-swift.enum)*