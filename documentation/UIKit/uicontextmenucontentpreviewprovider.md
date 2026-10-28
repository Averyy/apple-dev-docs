# UIContextMenuContentPreviewProvider

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

Returns the custom view controller to use when previewing your content.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
typealias UIContextMenuContentPreviewProvider = () -> UIViewController?
```

```c
typedef UIViewController *(^)(void) UIContextMenuContentPreviewProvider;
```

## Return Value

The view controller to display in place of the system’s standard view controller. If you want UIKit to present your content using a default view controller, return `nil`.

## Discussion

Use this handler to load or create your custom view controller, configure it with your content, and return it to UIKit.

## See Also

### Creating the menu configuration object
- [convenience init(identifier: (any NSCopying)?, previewProvider: UIContextMenuContentPreviewProvider?, actionProvider: UIContextMenuActionProvider?)](./uicontextmenuconfiguration/init%28identifier,previewprovider,actionprovider%29.md)
  Creates a menu configuration object with the specified action and preview providers.
- [typealias UIContextMenuActionProvider](./uicontextmenuactionprovider.md)
  Returns an action-based contextual menu, optionally incorporating the system-suggested actions.
- [+ configurationWithIdentifier:previewProvider:actionProvider:](./uicontextmenuconfiguration/configurationwithidentifier_previewprovider_actionprovider_.md)
  Creates a menu configuration object with the specified action and preview providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenucontentpreviewprovider)*