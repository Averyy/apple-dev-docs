# UIContentSizeCategory

**Framework**: UIKit  
**Kind**: struct

Constants that indicate the preferred size of your content.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct UIContentSizeCategory
```

## Topics

### Font sizes
- [static let unspecified: UIContentSizeCategory](uicontentsizecategory/unspecified.md)
  An unspecified font size.
- [static let extraSmall: UIContentSizeCategory](uicontentsizecategory/extrasmall.md)
  An extra-small font.
- [static let small: UIContentSizeCategory](uicontentsizecategory/small.md)
  A small font.
- [static let medium: UIContentSizeCategory](uicontentsizecategory/medium.md)
  A medium-sized font.
- [static let large: UIContentSizeCategory](uicontentsizecategory/large.md)
  A large font.
- [static let extraLarge: UIContentSizeCategory](uicontentsizecategory/extralarge.md)
  An extra-large font.
- [static let extraExtraLarge: UIContentSizeCategory](uicontentsizecategory/extraextralarge.md)
  A font that is larger than the extra-large font but smaller than the largest font size available.
- [static let extraExtraExtraLarge: UIContentSizeCategory](uicontentsizecategory/extraextraextralarge.md)
  The largest font size.
### Accessibility sizes
- [static let accessibilityMedium: UIContentSizeCategory](uicontentsizecategory/accessibilitymedium.md)
  A medium font size that reflects the current accessibility settings.
- [static let accessibilityLarge: UIContentSizeCategory](uicontentsizecategory/accessibilitylarge.md)
  A large font size that reflects the current accessibility settings.
- [static let accessibilityExtraLarge: UIContentSizeCategory](uicontentsizecategory/accessibilityextralarge.md)
  An extra-large font size that reflects the current accessibility settings.
- [static let accessibilityExtraExtraLarge: UIContentSizeCategory](uicontentsizecategory/accessibilityextraextralarge.md)
  A font that is larger than the extra-large font but not the largest available, reflecting the current accessibility settings.
- [static let accessibilityExtraExtraExtraLarge: UIContentSizeCategory](uicontentsizecategory/accessibilityextraextraextralarge.md)
  The largest font size that reflects the current accessibility settings.
- [var isAccessibilityCategory: Bool](uicontentsizecategory/isaccessibilitycategory.md)
  A Boolean value that indicates whether the content size category is associated with accessibility.
### Font size change notifications
- [static let didChangeNotification: NSNotification.Name](uicontentsizecategory/didchangenotification.md)
  A notification that posts when the user changes the preferred content size setting.
- [static let newValueUserInfoKey: String](uicontentsizecategory/newvalueuserinfokey.md)
  A key that reflects the new preferred content size.
### Font size category creation
- [init(rawValue: String)](uicontentsizecategory/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [init(ContentSizeCategory?)](uicontentsizecategory/init(_:)-9l1kn.md)
  Creates a content size category from the specified SwiftUI content size category.
- [init(DynamicTypeSize?)](uicontentsizecategory/init(_:)-abz4.md)
  Creates a content size category from the specified SwiftUI Dynamic Type size.
### Structures
- [UIContentSizeCategory.DidChangeMessage](uicontentsizecategory/didchangemessage.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var preferredContentSizeCategory: UIContentSizeCategory](uiapplication/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [protocol UIContentSizeCategoryAdjusting](uicontentsizecategoryadjusting.md)
  A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.
- [static let didChangeNotification: NSNotification.Name](uicontentsizecategory/didchangenotification.md)
  A notification that posts when the user changes the preferred content size setting.
- [static let newValueUserInfoKey: String](uicontentsizecategory/newvalueuserinfokey.md)
  A key that reflects the new preferred content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentsizecategory)*