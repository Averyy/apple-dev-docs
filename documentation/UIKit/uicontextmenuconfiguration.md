# UIContextMenuConfiguration

**Framework**: UIKit  
**Kind**: class

An object containing the configuration details for the contextual menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIContextMenuConfiguration
```

#### Overview

Before displaying a contextual menu, the system asks your [`UIContextMenuInteractionDelegate`](uicontextmenuinteractiondelegate.md) to provide a [`UIContextMenuConfiguration`](uicontextmenuconfiguration.md) object with details about that menu. In your [`contextMenuInteraction(_:configurationForMenuAtLocation:)`](uicontextmenuinteractiondelegate/contextmenuinteraction(_:configurationformenuatlocation:).md) method, use the location parameter to determine where the interaction occurred, and use the content at that location to configure your contextual menu and view controller. Provide custom blocks to generate:

- The contextual menu with the actions for your content.
- An optional view controller to use when displaying your content.

If you specify a default object without any custom handler blocks, the system displays a default preview interface with no menu.

## Topics

### Creating the menu configuration object
- [convenience init(identifier: (any NSCopying)?, previewProvider: UIContextMenuContentPreviewProvider?, actionProvider: UIContextMenuActionProvider?)](uicontextmenuconfiguration/init(identifier:previewprovider:actionprovider:).md)
  Creates a menu configuration object with the specified action and preview providers.
- [typealias UIContextMenuContentPreviewProvider](uicontextmenucontentpreviewprovider.md)
  Returns the custom view controller to use when previewing your content.
- [typealias UIContextMenuActionProvider](uicontextmenuactionprovider.md)
  Returns an action-based contextual menu, optionally incorporating the system-suggested actions.
### Getting the configuration identifier
- [var identifier: any NSCopying](uicontextmenuconfiguration/identifier.md)
  The unique identifier for this configuration object.
### Handling multiple-item interactions
- [var secondaryItemIdentifiers: Set<AnyHashable>](uicontextmenuconfiguration/secondaryitemidentifiers.md)
  A set of identifiers corresponding to each item other than the primary item in a multiple-item interaction.
- [var badgeCount: Int](uicontextmenuconfiguration/badgecount.md)
  The number of items in a multiple-item interaction.
### Specifying the order of menu elements
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](uicontextmenuconfiguration/preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.
- [UIContextMenuConfiguration.ElementOrder](uicontextmenuconfiguration/elementorder.md)
  Constants that define the ordering strategy for menu elements in a context menu.
### Instance Properties
- [var allowsTypeSelect: Bool](uicontextmenuconfiguration/allowstypeselect.md)
  A Boolean value that indicates whether the context menu supports keystroke-based navigation.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [func contextMenuInteraction(UIContextMenuInteraction, configurationForMenuAtLocation: CGPoint) -> UIContextMenuConfiguration?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:configurationformenuatlocation:).md)
  Returns the configuration data to use when previewing the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration)*