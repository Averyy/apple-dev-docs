# DynamicTypeSize

**Framework**: SwiftUI  
**Kind**: enum

A Dynamic Type size, which specifies how large scalable content should be.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum DynamicTypeSize
```

#### Overview

For more information, see [`Typography`](https://developer.apple.com/design/Human-Interface-Guidelines/typography) in the Human Interface Guidelines.

## Topics

### Getting type sizes
- [DynamicTypeSize.xSmall](dynamictypesize/xsmall.md)
  An extra small size.
- [DynamicTypeSize.small](dynamictypesize/small.md)
  A small size.
- [DynamicTypeSize.medium](dynamictypesize/medium.md)
  A medium size.
- [DynamicTypeSize.large](dynamictypesize/large.md)
  A large size.
- [DynamicTypeSize.xLarge](dynamictypesize/xlarge.md)
  An extra large size.
- [DynamicTypeSize.xxLarge](dynamictypesize/xxlarge.md)
  An extra extra large size.
- [DynamicTypeSize.xxxLarge](dynamictypesize/xxxlarge.md)
  An extra extra extra large size.
### Getting accessibility type sizes
- [DynamicTypeSize.accessibility1](dynamictypesize/accessibility1.md)
  The first accessibility size.
- [DynamicTypeSize.accessibility2](dynamictypesize/accessibility2.md)
  The second accessibility size.
- [DynamicTypeSize.accessibility3](dynamictypesize/accessibility3.md)
  The third accessibility size.
- [DynamicTypeSize.accessibility4](dynamictypesize/accessibility4.md)
  The fourth accessibility size.
- [DynamicTypeSize.accessibility5](dynamictypesize/accessibility5.md)
  The fifth accessibility size.
- [var isAccessibilitySize: Bool](dynamictypesize/isaccessibilitysize.md)
  A Boolean value indicating whether the size is one that is associated with accessibility.
### Creating a type size
- [init?(UIContentSizeCategory)](dynamictypesize/init(_:).md)
  Create a Dynamic Type size from its `UIContentSizeCategory` equivalent.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func textScale(Text.Scale, isEnabled: Bool) -> some View](view/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func dynamicTypeSize(_:)](view/dynamictypesize(_:).md)
  Sets the Dynamic Type size within the view to the given value.
- [var dynamicTypeSize: DynamicTypeSize](environmentvalues/dynamictypesize.md)
  The current Dynamic Type size.
- [struct ScaledMetric](scaledmetric.md)
  A dynamic property that scales a numeric value.
- [protocol TextVariantPreference](textvariantpreference.md)
  A protocol for controlling the size variant of text views.
- [struct FixedTextVariant](fixedtextvariant.md)
  The default text variant preference that chooses the largest available variant.
- [struct SizeDependentTextVariant](sizedependenttextvariant.md)
  The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamictypesize)*