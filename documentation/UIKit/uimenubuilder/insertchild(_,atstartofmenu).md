# insertChild(_:atStartOfMenu:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
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
func insertChild(_ childMenu: UIMenu, atStartOfMenu parentIdentifier: UIMenu.Identifier)
```

```objc
- (void) insertChildMenu:(UIMenu *) childMenu atStartOfMenuForIdentifier:(UIMenuIdentifier) parentIdentifier;
```

## Parameters

- `childMenu`: The child menu to insert.
- `parentIdentifier`: The identifier of the parent menu in which to insert the child menu.

## See Also

### Inserting child menus
- [func insertChild(UIMenu, atEndOfMenu: UIMenu.Identifier)](./insertchild%28_,atendofmenu%29.md)
  Adds a child menu as the last element of the specified parent menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertchild(_:atstartofmenu:))*