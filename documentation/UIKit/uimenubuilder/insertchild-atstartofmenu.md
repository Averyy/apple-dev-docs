# insertChild(_:atStartOfMenu:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Adds a child menu as the first element of the specified parent menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func insertChild(_ childMenu: UIMenu, atStartOfMenu parentIdentifier: UIMenu.Identifier)
```

## Parameters

- `childMenu`: The child menu to insert.
- `parentIdentifier`: The identifier of the parent menu in which to insert the child menu.

## See Also

- [func insertChild(UIMenu, atEndOfMenu: UIMenu.Identifier)](uimenubuilder/insertchild(_:atendofmenu:).md)
  Adds a child menu as the last element of the specified parent menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertchild(_:atstartofmenu:))*