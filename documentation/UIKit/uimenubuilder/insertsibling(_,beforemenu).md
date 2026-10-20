# insertSibling(_:beforeMenu:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Inserts a sibling menu before the specified menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func insertSibling(_ siblingMenu: UIMenu, beforeMenu siblingIdentifier: UIMenu.Identifier)
```

```objc
- (void) insertSiblingMenu:(UIMenu *) siblingMenu beforeMenuForIdentifier:(UIMenuIdentifier) siblingIdentifier;
```

## Parameters

- `siblingMenu`: The sibling menu to insert.
- `siblingIdentifier`: The identifier of the menu that comes after the inserted sibling menu.

## See Also

### Inserting sibling menus
- [func insertSibling(UIMenu, afterMenu: UIMenu.Identifier)](./insertsibling%28_,aftermenu%29.md)
  Inserts a sibling menu after the specified menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertsibling(_:beforemenu:))*