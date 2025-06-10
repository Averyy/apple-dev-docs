# sharesBackground

**Framework**: UIKit  
**Kind**: property

A boolean value indicating whether this bar button item can share a background with other items in a navigation bar or a toolbar.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
var sharesBackground: Bool { get set }
```

#### Discussion

When `NO`, This item will not be visually grouped with any other items.

This property is ignored if the item is in a `UIBarButtonItemGroup` with more than one item. The default value is `YES`.

## See Also

- [var hidesSharedBackground: Bool](uibarbuttonitem/hidessharedbackground.md)
  A boolean value indicating whether the background this item may share with other items in the bar should be hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/sharesbackground)*