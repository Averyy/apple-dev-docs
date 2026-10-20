# ContentSizeCategory

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

The sizes that you can specify for content.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: DynamicTypeSize)
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: DynamicTypeSize)
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: DynamicTypeSize)
- macOS 10.15+ - Deprecated in 27.2 (renamed: DynamicTypeSize)
- tvOS 13.0+ - Deprecated in 27.2 (renamed: DynamicTypeSize)
- visionOS 1.0+ - Deprecated in 27.2 (renamed: DynamicTypeSize)
- watchOS 6.0+ - Deprecated in 27.2 (renamed: DynamicTypeSize)

> **Deprecated**: Use [`DynamicTypeSize`](./dynamictypesize.md) instead.

## Declaration

```swift
enum ContentSizeCategory
```

## Topics

### Content size categories
- [ContentSizeCategory.accessibilityExtraExtraExtraLarge](./contentsizecategory/accessibilityextraextraextralarge.md)
- [ContentSizeCategory.accessibilityExtraExtraLarge](./contentsizecategory/accessibilityextraextralarge.md)
- [ContentSizeCategory.accessibilityExtraLarge](./contentsizecategory/accessibilityextralarge.md)
- [ContentSizeCategory.accessibilityLarge](./contentsizecategory/accessibilitylarge.md)
- [ContentSizeCategory.accessibilityMedium](./contentsizecategory/accessibilitymedium.md)
- [ContentSizeCategory.extraExtraExtraLarge](./contentsizecategory/extraextraextralarge.md)
- [ContentSizeCategory.extraExtraLarge](./contentsizecategory/extraextralarge.md)
- [ContentSizeCategory.extraLarge](./contentsizecategory/extralarge.md)
- [ContentSizeCategory.extraSmall](./contentsizecategory/extrasmall.md)
- [ContentSizeCategory.large](./contentsizecategory/large.md)
- [ContentSizeCategory.medium](./contentsizecategory/medium.md)
- [ContentSizeCategory.small](./contentsizecategory/small.md)
### Creating a size category
- [init?(UIContentSizeCategory)](./contentsizecategory/init%28_%29.md)
  Create a size category from its UIContentSizeCategory equivalent.
### Comparing content size categories
- [var isAccessibilityCategory: Bool](./contentsizecategory/isaccessibilitycategory.md)
  A Boolean value indicating whether the content size category is one that is associated with accessibility.
### Operators
- [static func < (ContentSizeCategory, ContentSizeCategory) -> Bool](./contentsizecategory/op%28_,_%29-1iyos.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (ContentSizeCategory, ContentSizeCategory) -> Bool](./contentsizecategory/op%28_,_%29-61nui.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func <= (ContentSizeCategory, ContentSizeCategory) -> Bool](./contentsizecategory/opeq%28_,_%29-3lvd8.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func >= (ContentSizeCategory, ContentSizeCategory) -> Bool](./contentsizecategory/opeq%28_,_%29-3tkt4.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.

## Relationships

### Conforms To
- [CaseIterable](../Swift/caseiterable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adjusting text size
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](./view/textscale%28_,isenabled%29.md)
  Applies a text scale to text in the view.
- [func dynamicTypeSize(_:)](./view/dynamictypesize%28_%29.md)
  Sets the Dynamic Type size within the view to the given value.
- [var dynamicTypeSize: DynamicTypeSize](./environmentvalues/dynamictypesize.md)
  The current Dynamic Type size.
- [enum DynamicTypeSize](./dynamictypesize.md)
  A Dynamic Type size, which specifies how large scalable content should be.
- [struct ScaledMetric](./scaledmetric.md)
  A dynamic property that scales a numeric value.
- [protocol TextVariantPreference](./textvariantpreference.md)
  A protocol for controlling the size variant of text views.
- [struct FixedTextVariant](./fixedtextvariant.md)
  The default text variant preference that chooses the largest available variant.
- [struct SizeDependentTextVariant](./sizedependenttextvariant.md)
  The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentsizecategory)*