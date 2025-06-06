# UIContextMenuContentPreviewProvider

**Framework**: UIKit  
**Kind**: typealias

Returns the custom view controller to use when previewing your content.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias UIContextMenuContentPreviewProvider = () -> UIViewController?
```

#### Return Value

The view controller to display in place of the system’s standard view controller. If you want UIKit to present your content using a default view controller, return `nil`.

#### Discussion

Use this handler to load or create your custom view controller, configure it with your content, and return it to UIKit.

## See Also

- [convenience init(identifier: (any NSCopying)?, previewProvider: UIContextMenuContentPreviewProvider?, actionProvider: UIContextMenuActionProvider?)](uicontextmenuconfiguration/init(identifier:previewprovider:actionprovider:).md)
  Creates a menu configuration object with the specified action and preview providers.
- [typealias UIContextMenuActionProvider](uicontextmenuactionprovider.md)
  Returns an action-based contextual menu, optionally incorporating the system-suggested actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenucontentpreviewprovider)*