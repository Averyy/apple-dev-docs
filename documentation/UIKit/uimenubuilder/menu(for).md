# menu(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the menu for the specified menu identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func menu(for identifier: UIMenu.Identifier) -> UIMenu?
```

```objc
- (UIMenu *) menuForIdentifier:(UIMenuIdentifier) identifier;
```

#### Return Value

A menu object; otherwise, `nil` if there are no menus with the specified identifier.

## Parameters

- `identifier`: The identifier of the menu to retrieve.

## See Also

### Getting menu systems and elements
- [var system: UIMenuSystem](./system.md)
  The menu system that the menu builder modifies.
- [func action(for: UIAction.Identifier) -> UIAction?](./action%28for%29.md)
  Gets the action for the specified action identifier.
- [func command(for: Selector, propertyList: Any?) -> UICommand?](./command%28for,propertylist%29.md)
  Gets the command for the specified selector and property list.
- [- commandForAction:propertyList:](./commandforaction_propertylist_.md)
  Gets the command for the specified selector and property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/menu(for:))*