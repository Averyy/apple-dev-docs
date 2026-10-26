# UIContentSizeCategoryCompareToCategory

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Compares two content size category values to determine whether they are equal or whether one is larger than the other.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```c
extern NSComparisonResult UIContentSizeCategoryCompareToCategory(UIContentSizeCategory lhs, UIContentSizeCategory rhs);
```

## See Also

### Retrieving content size category information
- [var preferredContentSizeCategory: UIContentSizeCategory](./uitraitcollection/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [struct UIContentSizeCategory](./uicontentsizecategory.md)
  Constants that indicate the preferred size of your content.
- [UIContentSizeCategoryIsAccessibilityCategory](./uicontentsizecategoryisaccessibilitycategory.md)
  Returns a Boolean value that indicates whether the content size category belongs to the group of accessibility-related sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentsizecategorycomparetocategory)*