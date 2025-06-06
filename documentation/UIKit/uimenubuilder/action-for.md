# action(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Gets the action for the specified action identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func action(for identifier: UIAction.Identifier) -> UIAction?
```

#### Return Value

An action object; otherwise, `nil` if there are no actions with the specified identifier.

## Parameters

- `identifier`: The identifier of the action to retrieve.

## See Also

- [var system: UIMenuSystem](uimenubuilder/system.md)
  The menu system that the menu builder modifies.
- [func menu(for: UIMenu.Identifier) -> UIMenu?](uimenubuilder/menu(for:).md)
  Gets the menu for the specified menu identifier.
- [func command(for: Selector, propertyList: Any?) -> UICommand?](uimenubuilder/command(for:propertylist:).md)
  Gets the command for the specified selector and property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/action(for:))*