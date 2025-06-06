# init(identifier:previewProvider:actionProvider:)

**Framework**: UIKit  
**Kind**: init

Creates a menu configuration object with the specified action and preview providers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(identifier: (any NSCopying)? = nil, previewProvider: UIContextMenuContentPreviewProvider? = nil, actionProvider: UIContextMenuActionProvider? = nil)
```

#### Return Value

A new menu configuration object with the specified provider blocks.

## Parameters

- `identifier`: A unique identifier for the menu configuration object. If you want this method to generate a unique identifier for you, specify  .
- `previewProvider`: An optional block that returns the custom view controller that you use to preview content. If you specify  , UIKit uses a default preview view controller.
- `actionProvider`: An optional block that provides a contextual menu to display with the preview. If you specify  , UIKit doesn’t display a contextual menu with the previewed content.

## See Also

- [typealias UIContextMenuContentPreviewProvider](uicontextmenucontentpreviewprovider.md)
  Returns the custom view controller to use when previewing your content.
- [typealias UIContextMenuActionProvider](uicontextmenuactionprovider.md)
  Returns an action-based contextual menu, optionally incorporating the system-suggested actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/init(identifier:previewprovider:actionprovider:))*