# commandForAction:propertyList:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Gets the command for the specified selector and property list.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
- (UICommand *) commandForAction:(SEL) action propertyList:(id) propertyList;
```

## Return Value

A command object; otherwise, `nil` if there is no such command.

## Parameters

- `action`: The selector of the command to retrieve.
- `propertyList`: The property list object that distinguish the command.

## See Also

### Getting menu systems and elements
- [var system: UIMenuSystem](./system.md)
  The menu system that the menu builder modifies.
- [func menu(for: UIMenu.Identifier) -> UIMenu?](./menu%28for%29.md)
  Gets the menu for the specified menu identifier.
- [func action(for: UIAction.Identifier) -> UIAction?](./action%28for%29.md)
  Gets the action for the specified action identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/commandforaction:propertylist:)*