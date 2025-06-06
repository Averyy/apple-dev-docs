# replace(menu:with:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Replaces the specified menu with a new menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func replace(menu replacedIdentifier: UIMenu.Identifier, with replacementMenu: UIMenu)
```

## Parameters

- `replacedIdentifier`: The identifier of the menu to replace.
- `replacementMenu`: The replacement menu.

## See Also

- [func replaceChildren(ofMenu: UIMenu.Identifier, from: ([UIMenuElement]) -> [UIMenuElement])](uimenubuilder/replacechildren(ofmenu:from:).md)
  Replaces the elements in a menu with the elements returned by the specified handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/replace(menu:with:))*