# ImagePlaygroundOptions.Personalization

**Framework**: Image Playground  
**Kind**: enum

An option for enabling or disabling people support in the system interface.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
enum Personalization
```

#### Overview

Enabling people support will allow the user to condition image generation using:

- A person from their system Photos library
- A character represented by an appearance and a skin tone

Personalization options are available through several user interfaces, including:

- A people picker
- Detection of people names in the prompt text field
- Importing images containing people faces from the system photo library

Use this type to configure the personalization behavior for the view controllers and SwiftUI view modifiers you use in your interface, or when interacting with an `ImageCreator` instance.

## Topics

### Enumeration Cases
- [ImagePlaygroundOptions.Personalization.automatic](imageplaygroundoptions/personalization-swift.enum/automatic.md)
  An option to choose the most appropriate personalization behavior.
- [ImagePlaygroundOptions.Personalization.disabled](imageplaygroundoptions/personalization-swift.enum/disabled.md)
  An option to disable personalization features in the view controller.
- [ImagePlaygroundOptions.Personalization.enabled](imageplaygroundoptions/personalization-swift.enum/enabled.md)
  An option to enable personalization features in the view controller.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/personalization-swift.enum)*