# didChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when the user changes the preferred content size setting.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let didChangeNotification: NSNotification.Name
```

## Mentions

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)

#### Discussion

This notification is sent when the value in the [`preferredContentSizeCategory`](uiapplication/preferredcontentsizecategory.md) property changes. The `userInfo` dictionary of the notification contains the [`newValueUserInfoKey`](uicontentsizecategory/newvalueuserinfokey.md) key, which reflects the new setting.

## See Also

- [var preferredContentSizeCategory: UIContentSizeCategory](uiapplication/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [struct UIContentSizeCategory](uicontentsizecategory.md)
  Constants that indicate the preferred size of your content.
- [protocol UIContentSizeCategoryAdjusting](uicontentsizecategoryadjusting.md)
  A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.
- [static let newValueUserInfoKey: String](uicontentsizecategory/newvalueuserinfokey.md)
  A key that reflects the new preferred content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentsizecategory/didchangenotification)*