# newValueUserInfoKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key that reflects the new preferred content size.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let newValueUserInfoKey: String
```

```c
extern NSString * const UIContentSizeCategoryNewValueKey;
```

#### Discussion

This key’s value is an [`NSString`](../../Foundation/nsstring.md) object that reflects the new value of the [`preferredContentSizeCategory`](../uiapplication/preferredcontentsizecategory.md) property.

## See Also

### Managing the preferred content size
- [var preferredContentSizeCategory: UIContentSizeCategory](../uiapplication/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [struct UIContentSizeCategory](../uicontentsizecategory.md)
  Constants that indicate the preferred size of your content.
- [protocol UIContentSizeCategoryAdjusting](../uicontentsizecategoryadjusting.md)
  A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.
- [static let didChangeNotification: NSNotification.Name](./didchangenotification.md)
  A notification that posts when the user changes the preferred content size setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentsizecategory/newvalueuserinfokey)*