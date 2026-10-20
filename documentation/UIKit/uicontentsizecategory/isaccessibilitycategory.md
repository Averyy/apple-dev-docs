# isAccessibilityCategory

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the content size category is associated with accessibility.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS

## Declaration

```swift
var isAccessibilityCategory: Bool { get }
```

#### Discussion

This property is [`true`](../../Swift/true.md) for [`accessibilityMedium`](./accessibilitymedium.md), [`accessibilityLarge`](./accessibilitylarge.md), [`accessibilityExtraLarge`](./accessibilityextralarge.md), [`accessibilityExtraExtraLarge`](./accessibilityextraextralarge.md), and [`accessibilityExtraExtraExtraLarge`](./accessibilityextraextraextralarge.md). It is [`false`](../../Swift/false.md) for other values.

## See Also

### Accessibility sizes
- [static let accessibilityMedium: UIContentSizeCategory](./accessibilitymedium.md)
  A medium font size that reflects the current accessibility settings.
- [static let accessibilityLarge: UIContentSizeCategory](./accessibilitylarge.md)
  A large font size that reflects the current accessibility settings.
- [static let accessibilityExtraLarge: UIContentSizeCategory](./accessibilityextralarge.md)
  An extra-large font size that reflects the current accessibility settings.
- [static let accessibilityExtraExtraLarge: UIContentSizeCategory](./accessibilityextraextralarge.md)
  A font that is larger than the extra-large font but not the largest available, reflecting the current accessibility settings.
- [static let accessibilityExtraExtraExtraLarge: UIContentSizeCategory](./accessibilityextraextraextralarge.md)
  The largest font size that reflects the current accessibility settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentsizecategory/isaccessibilitycategory)*