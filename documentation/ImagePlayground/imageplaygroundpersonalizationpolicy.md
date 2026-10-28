# ImagePlaygroundPersonalizationPolicy

**Framework**: Image Playground  
**Kind**: enum  
**Role**: Enumeration

An option for enabling or disabling personalization in the system interface.

**Availability**:
- iOS 18.4+ - Deprecated in 26.4
- iPadOS 18.4+ - Deprecated in 26.4
- Mac Catalyst 18.4+ - Deprecated in 26.4
- macOS 15.4+ - Deprecated in 26.4
- visionOS 2.4+ - Deprecated in 26.4

> **Deprecated**: Use the ImagePlaygroundOptions.Personalization type.

## Declaration

```swift
enum ImagePlaygroundPersonalizationPolicy
```

## Overview

Use this type to configure the personalization behavior for the view controllers and SwiftUI view modifiers you use in your interface.

## Topics

### Getting the policy
- [ImagePlaygroundPersonalizationPolicy.automatic](./imageplaygroundpersonalizationpolicy/automatic.md)
  An option to choose the most appropriate personalization behavior.
- [ImagePlaygroundPersonalizationPolicy.enabled](./imageplaygroundpersonalizationpolicy/enabled.md)
  An option to enable personalization features in the view controller.
- [ImagePlaygroundPersonalizationPolicy.disabled](./imageplaygroundpersonalizationpolicy/disabled.md)
  An option to disable personalization features in the view controller.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)

## See Also

### Specifying the configuration of the playground
- [var selectedGenerationStyle: ImagePlaygroundStyle](./imageplaygroundviewcontroller/selectedgenerationstyle.md)
  Generation style to pre-select upong launching the playground among those in `allowedGenerationStyles`.
- [var allowedGenerationStyles: [ImagePlaygroundStyle]](./imageplaygroundviewcontroller/allowedgenerationstyles.md)
  A list of allowed generation styles to choose from in the playground.
- [var personalizationPolicy: ImagePlaygroundPersonalizationPolicy](./imageplaygroundviewcontroller/personalizationpolicy.md)
  The policy to apply when determining whether to include people in generated images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundpersonalizationpolicy)*