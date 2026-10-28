# ImagePlaygroundOptions.Personalization

**Framework**: Image Playground  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

The SwiftUI sheets, [`ImagePlaygroundViewController`](../imageplaygroundviewcontroller.md) type, and [`ImageCreator`](../imagecreator.md) type offer ways to personalize the images you create using an existing photo or other information. When configuring one of those types, create an instance of [`ImagePlaygroundOptions`](../imageplaygroundoptions.md) and configure its [`personalization`](./personalization-swift.property.md) property with your personalization preferences.

Personalization tells the system how to craft the appearance of people in the images it creates. The system can derive appearance choices for people from additional sources, such as from photos in the person’s Photos library. If you disable personalization, the system uses only the prompts and starting image you provide to generate the images.

## Topics

### Enumeration Cases
- [ImagePlaygroundOptions.Personalization.automatic](./personalization-swift.enum/automatic.md)
  An option to choose the most appropriate personalization behavior.
- [ImagePlaygroundOptions.Personalization.disabled](./personalization-swift.enum/disabled.md)
  An option to disable personalization features during image generation.
- [ImagePlaygroundOptions.Personalization.enabled](./personalization-swift.enum/enabled.md)
  An option to enable personalization features during image generation.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/personalization-swift.enum)*