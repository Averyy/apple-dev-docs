# command(for:propertyList:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Gets the command for the specified selector and property list.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func command(for action: Selector, propertyList: Any? = nil) -> UICommand?
```

#### Return Value

A command object; otherwise, `nil` if there is no such command.

## Parameters

- `action`: The selector of the command to retrieve.
- `propertyList`: The property list object that identifies the command when more than one command uses the same action.

## See Also

### Getting menu systems and elements
- [var system: UIMenuSystem](./system.md)
  The menu system that the menu builder modifies.
- [func menu(for: UIMenu.Identifier) -> UIMenu?](./menu%28for%29.md)
  Gets the menu for the specified menu identifier.
- [func action(for: UIAction.Identifier) -> UIAction?](./action%28for%29.md)
  Gets the action for the specified action identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/command(for:propertylist:))*