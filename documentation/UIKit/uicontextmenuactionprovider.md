# UIContextMenuActionProvider

**Framework**: UIKit  
**Kind**: typealias

Returns an action-based contextual menu, optionally incorporating the system-suggested actions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias UIContextMenuActionProvider = ([UIMenuElement]) -> UIMenu?
```

#### Return Value

The menu object containing the actions for the user to select.

#### Discussion

Use this handler to create [`UIAction`](uiaction.md) objects representing the actions the user may choose from your menu. To organize groups of actions hierarchically, create a [`UIMenu`](uimenu.md) object to represent a submenu and add nested actions to it. Finally, build your top-level [`UIMenu`](uimenu.md) object from the actions and submenus you created, and return that menu object from your handler.

## Parameters

- `suggestedActions`: Suggested actions for you to include in your menu. UIKit collects these actions from responders in the current responder chain. You are not required to include the actions in your menu.

## See Also

- [convenience init(identifier: (any NSCopying)?, previewProvider: UIContextMenuContentPreviewProvider?, actionProvider: UIContextMenuActionProvider?)](uicontextmenuconfiguration/init(identifier:previewprovider:actionprovider:).md)
  Creates a menu configuration object with the specified action and preview providers.
- [typealias UIContextMenuContentPreviewProvider](uicontextmenucontentpreviewprovider.md)
  Returns the custom view controller to use when previewing your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuactionprovider)*