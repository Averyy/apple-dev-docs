# UINavigationItem.ItemStyle

**Framework**: UIKit  
**Kind**: enum

Constants that determine how the content of the navigation item lays out in the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum ItemStyle
```

#### Overview

Navigation styles allow you to customize the behavior and content density of your navigation bar according to your app type.

- Navigator apps like Settings support a traditional navigation model for hierarchical data.
- Browser apps like Safari or Files support browsing through and navigating back and forth between multiple documents or folder structures.
- Editor apps support focused viewing or editing of individual documents.

> **Note**:  Session 10069: [`Meet desktop-class iPad`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10069) Session 10070: [`Build a desktop-class iPad app`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10070)

 Session 10069: [`Meet desktop-class iPad`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10069)

Session 10070: [`Build a desktop-class iPad app`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10070)

## Topics

### Constants
- [UINavigationItem.ItemStyle.navigator](uinavigationitem/itemstyle/navigator.md)
  A style for a traditional navigation-based interface.
- [UINavigationItem.ItemStyle.browser](uinavigationitem/itemstyle/browser.md)
  A style for a browser app interface.
- [UINavigationItem.ItemStyle.editor](uinavigationitem/itemstyle/editor.md)
  A style for an editor app interface.
### Initializers
- [init?(rawValue: Int)](uinavigationitem/itemstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var style: UINavigationItem.ItemStyle](uinavigationitem/style.md)
  A style that determines how the content of the navigation item lays out in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/itemstyle)*