# isAccessibilityCategory

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the content size category is associated with accessibility.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
var isAccessibilityCategory: Bool { get }
```

#### Discussion

This property is [`true`](https://developer.apple.com/documentation/Swift/true) for [`accessibilityMedium`](uicontentsizecategory/accessibilitymedium.md), [`accessibilityLarge`](uicontentsizecategory/accessibilitylarge.md), [`accessibilityExtraLarge`](uicontentsizecategory/accessibilityextralarge.md), [`accessibilityExtraExtraLarge`](uicontentsizecategory/accessibilityextraextralarge.md), and [`accessibilityExtraExtraExtraLarge`](uicontentsizecategory/accessibilityextraextraextralarge.md). It is [`false`](https://developer.apple.com/documentation/Swift/false) for other values.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentsizecategory/isaccessibilitycategory)*