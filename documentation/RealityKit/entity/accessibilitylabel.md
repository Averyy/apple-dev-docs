# accessibilityLabel

**Framework**: RealityKit  
**Kind**: property

A succinct label that identifies the purpose of the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var accessibilityLabel: String? { get set }
```

## Mentions

- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)

#### Discussion

The default value for this property is `false`.

For entities with [`isAccessibilityElement`](entity/isaccessibilityelement.md) set to [`true`](https://developer.apple.com/documentation/Swift/true), iOS uses this string to provide information to users of assistive technologies like VoiceOver. Set this property to a name or short description that accurately describes the entity. If you wish to provide additional information or a longer description of the entity, you can use [`accessibilityDescription`](entity/accessibilitydescription.md).

## See Also

- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [var isAccessibilityElement: Bool](entity/isaccessibilityelement.md)
  A Boolean value indicating whether the receiver is an accessibility element that an assistive application can access.
- [var accessibilityLabelKey: LocalizedStringResource?](entity/accessibilitylabelkey.md)
  A succinct label that identifies the entity, in a localized string key.
- [var accessibilityCustomActions: [LocalizedStringResource]](entity/accessibilitycustomactions.md)
  An array of custom actions supported by the entity, identified by their localized string key.
- [var accessibilityCustomContent: [AccessibilityComponent.CustomContent]](entity/accessibilitycustomcontent.md)
  The Custom Content API is useful for delivering accessibility information from complex data sets to your users in measured portions. Using this API allows you to leverage assistive technologies to present only the accessible content your app’s users need, when they need it.
- [var accessibilityCustomRotors: [AccessibilityComponent.RotorType]](entity/accessibilitycustomrotors.md)
  An array of supported rotors.
- [var accessibilityLabelKey: LocalizedStringResource?](entity/accessibilitylabelkey.md)
  A succinct label that identifies the entity, in a localized string key.
- [var accessibilitySystemActions: AccessibilityComponent.SupportedActions](entity/accessibilitysystemactions.md)
  The set of supported accessibility actions.
- [var accessibilityTraits: UIAccessibilityTraits](entity/accessibilitytraits.md)
  The combination of accessibility traits that best characterize the entity.
- [var accessibilityValue: LocalizedStringResource?](entity/accessibilityvalue.md)
  A localized string key that represents the current value of the entity.
- [var accessibilityDescription: String?](entity/accessibilitydescription.md)
  A longer description of the entity for use by assistive technologies.
- [var accessibilityDescription: String?](entity/accessibilitydescription.md)
  A longer description of the entity for use by assistive technologies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/accessibilitylabel)*