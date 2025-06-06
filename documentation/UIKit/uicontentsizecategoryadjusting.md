# UIContentSizeCategoryAdjusting

**Framework**: UIKit  
**Kind**: protocol

A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIContentSizeCategoryAdjusting : NSObjectProtocol
```

## Topics

### Adjusting the size of fonts
- [var adjustsFontForContentSizeCategory: Bool](uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory.md)
  A Boolean that indicates whether the object automatically updates its font when the device’s content size category changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UILabel](uilabel.md)
- [UISearchTextField](uisearchtextfield.md)
- [UITextField](uitextfield.md)
- [UITextView](uitextview.md)

## See Also

- [var preferredContentSizeCategory: UIContentSizeCategory](uiapplication/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [struct UIContentSizeCategory](uicontentsizecategory.md)
  Constants that indicate the preferred size of your content.
- [static let didChangeNotification: NSNotification.Name](uicontentsizecategory/didchangenotification.md)
  A notification that posts when the user changes the preferred content size setting.
- [static let newValueUserInfoKey: String](uicontentsizecategory/newvalueuserinfokey.md)
  A key that reflects the new preferred content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting)*