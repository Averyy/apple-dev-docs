# menu

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The context menu for this button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var menu: UIMenu? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UIMenu * menu;
```

#### Discussion

The context menu displays in response to a person tapping the item.

## See Also

### Managing the context menu
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](./preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/menu)*