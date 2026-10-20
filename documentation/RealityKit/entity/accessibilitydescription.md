# accessibilityDescription

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A longer description of the entity for use by assistive technologies.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0 (renamed: accessibilityCustomContent)
- iPadOS 14.0+ - Deprecated in 17.0 (renamed: accessibilityCustomContent)
- Mac Catalyst 14.0+ - Deprecated in 17.0 (renamed: accessibilityCustomContent)
- macOS 11.0+ - Deprecated in 14.0 (renamed: accessibilityCustomContent)
- visionOS - Deprecated in 1.0 (renamed: accessibilityCustomContent)

## Declaration

```swift
@MainActor
@preconcurrency var accessibilityDescription: String? { get set }
```

## Mentions

- [Improving the Accessibility of RealityKit Apps](../improving-the-accessibility-of-realitykit-apps.md)

## See Also

### Configuring accessibility features
- [Improving the Accessibility of RealityKit Apps](../improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [var isAccessibilityElement: Bool](./isaccessibilityelement.md)
  A Boolean value indicating whether the receiver is an accessibility element that an assistive application can access.
- [var accessibilityLabelKey: LocalizedStringResource?](./accessibilitylabelkey.md)
  A succinct label that identifies the entity, in a localized string key.
- [var accessibilityCustomActions: [LocalizedStringResource]](./accessibilitycustomactions.md)
  An array of custom actions supported by the entity, identified by their localized string key.
- [var accessibilityCustomContent: [AccessibilityComponent.CustomContent]](./accessibilitycustomcontent.md)
  The Custom Content API is useful for delivering accessibility information from complex data sets to your users in measured portions. Using this API allows you to leverage assistive technologies to present only the accessible content your app’s users need, when they need it.
- [var accessibilityCustomRotors: [AccessibilityComponent.RotorType]](./accessibilitycustomrotors.md)
  An array of supported rotors.
- [var accessibilityLabelKey: LocalizedStringResource?](./accessibilitylabelkey.md)
  A succinct label that identifies the entity, in a localized string key.
- [var accessibilitySystemActions: AccessibilityComponent.SupportedActions](./accessibilitysystemactions.md)
  The set of supported accessibility actions.
- [var accessibilityTraits: UIAccessibilityTraits](./accessibilitytraits.md)
  The combination of accessibility traits that best characterize the entity.
- [var accessibilityValue: LocalizedStringResource?](./accessibilityvalue.md)
  A localized string key that represents the current value of the entity.
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A succinct label that identifies the purpose of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/accessibilitydescription)*