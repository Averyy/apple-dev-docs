# menu(for:)

**Framework**: UIKit  
**Kind**: method  
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
@MainActor
func menu(for identifier: UIMenu.Identifier) -> UIMenu?
```

#### Return Value

A menu object; otherwise, `nil` if there are no menus with the specified identifier.

## Parameters

- `identifier`: The identifier of the menu to retrieve.

## See Also

- [var system: UIMenuSystem](uimenubuilder/system.md)
  The menu system that the menu builder modifies.
- [func action(for: UIAction.Identifier) -> UIAction?](uimenubuilder/action(for:).md)
  Gets the action for the specified action identifier.
- [func command(for: Selector, propertyList: Any?) -> UICommand?](uimenubuilder/command(for:propertylist:).md)
  Gets the command for the specified selector and property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/menu(for:))*