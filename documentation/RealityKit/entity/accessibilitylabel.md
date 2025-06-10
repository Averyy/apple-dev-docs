# accessibilityLabel

**Framework**: RealityKit  
**Kind**: property

A succinct label that identifies the purpose of the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+ (Beta)
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

For entities with [`isAccessibilityElement`](entity/isaccessibilityelement.md) set to [`true`](https://developer.apple.com/documentation/swift/true), iOS uses this string to provide information to users of assistive technologies like VoiceOver. Set this property to a name or short description that accurately describes the entity. If you wish to provide additional information or a longer description of the entity, you can use [`accessibilityDescription`](entity/accessibilitydescription.md).

## See Also

- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [var isAccessibilityElement: Bool](entity/isaccessibilityelement.md)
  A Boolean value indicating whether the receiver is an accessibility element that an assistive application can access.
- [var accessibilityDescription: String?](entity/accessibilitydescription.md)
  A longer description of the entity for use by assistive technologies.
- [var accessibilityDescription: String?](entity/accessibilitydescription.md)
  A longer description of the entity for use by assistive technologies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/accessibilitylabel)*