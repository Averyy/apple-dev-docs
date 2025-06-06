# insertSibling(_:afterMenu:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Inserts a sibling menu after the specified menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func insertSibling(_ siblingMenu: UIMenu, afterMenu siblingIdentifier: UIMenu.Identifier)
```

## Parameters

- `siblingMenu`: The sibling menu to insert.
- `siblingIdentifier`: The identifier of the menu that comes before the inserted sibling menu.

## See Also

- [func insertSibling(UIMenu, beforeMenu: UIMenu.Identifier)](uimenubuilder/insertsibling(_:beforemenu:).md)
  Inserts a sibling menu before the specified menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertsibling(_:aftermenu:))*