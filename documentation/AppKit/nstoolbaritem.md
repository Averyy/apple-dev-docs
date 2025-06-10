# NSToolbarItem

**Framework**: AppKit  
**Kind**: class

A single item that appears in a window’s toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
class NSToolbarItem
```

#### Overview

An [`NSToolbarItem`](nstoolbaritem.md) object displays an image and text string in the toolbar area of a window. You can also create toolbar items that display custom views you provide. Toolbar items provide fast access to common commands or features in the window. For example, the Finder window uses toolbar items to help someone navigate the file system.

You typically create toolbar items at the same time you create your window’s toolbar. The system provides some standard items like spacers you can include in your toolbar. It also provides items that display standard interfaces like the color panel or font panel. For any custom toolbar items you create, provide an action method to call when someone clicks the item.

You can display your toolbar item’s content using a custom view if you prefer, rather than an image and text label. If you specify an [`NSSearchField`](nssearchfield.md) object for the view, the system automatically adjusts the minimum and maximum size of the search field to the system-standard values.

## Topics

### Creating a toolbar item
- [init(itemIdentifier: NSToolbarItem.Identifier)](nstoolbaritem/init(itemidentifier:).md)
  Creates a toolbar item with the specified identifier.
- [convenience init(itemIdentifier: NSToolbarItem.Identifier, barButtonItem: UIBarButtonItem)](nstoolbaritem/init(itemidentifier:barbuttonitem:).md)
  Creates a toolbar item with property values from the specified bar button item.
### Getting the toolbar item’s identity
- [var itemIdentifier: NSToolbarItem.Identifier](nstoolbaritem/itemidentifier.md)
  The value you use to identify the toolbar item.
- [NSToolbarItem.Identifier](nstoolbaritem/identifier.md)
  Constants for the standard toolbar items that the system provides.
### Describing the item
- [var possibleLabels: Set<String>](nstoolbaritem/possiblelabels.md)
  The set of labels that the item might display.
- [var label: String](nstoolbaritem/label.md)
  The label that appears for this item in the toolbar.
- [var paletteLabel: String](nstoolbaritem/palettelabel.md)
  The label that appears when the toolbar item is in the customization palette.
- [var title: String](nstoolbaritem/title.md)
  The title of the toolbar item.
- [var toolTip: String?](nstoolbaritem/tooltip.md)
  The tooltip to display when someone hovers over the item in the toolbar.
### Getting the item’s visual appearance
- [var image: UIImage?](nstoolbaritem/image.md)
  The image to display for the toolbar item.
- [var backgroundTintColor: UIColor?](nstoolbaritem/backgroundtintcolor.md)
- [var view: NSView?](nstoolbaritem/view.md)
  The custom view you use to draw the toolbar item.
### Performing the item’s action
- [var target: AnyObject?](nstoolbaritem/target.md)
  The object that defines the action method the toolbar item calls when clicked.
- [var action: Selector?](nstoolbaritem/action.md)
  The action method to call when someone clicks on the toolbar item.
### Configuring the item’s menu
- [var menuFormRepresentation: NSMenuItem?](nstoolbaritem/menuformrepresentation.md)
  The menu item to use when the toolbar item is in the overflow menu.
- [var itemMenuFormRepresentation: UIMenuElement?](nstoolbaritem/itemmenuformrepresentation.md)
  The menu item to use for the toolbar item is in the overflow menu in a Mac app built with Mac Catalyst.
### Getting the item’s configuration
- [var isVisible: Bool](nstoolbaritem/isvisible.md)
  A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [var isHidden: Bool](nstoolbaritem/ishidden.md)
- [var isBordered: Bool](nstoolbaritem/isbordered.md)
  A Boolean value that indicates whether the toolbar item has a bordered style.
- [var isNavigational: Bool](nstoolbaritem/isnavigational.md)
  A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.
- [var isEnabled: Bool](nstoolbaritem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
- [var style: NSToolbarItem.Style](nstoolbaritem/style-swift.property.md)
  Defines the toolbar item’s appearance. The default style is plain. Prominent style tints the background. If a background tint color is set, it uses it; otherwise, it uses the app’s or system’s accent color. If grouped with other items, it moves to its own to avoid tinting other items’ background.
- [NSToolbarItem.Style](nstoolbaritem/style-swift.enum.md)
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [var tag: Int](nstoolbaritem/tag.md)
  An integer tag you can use to identify the toolbar item.
### Getting the parent toolbar
- [var toolbar: NSToolbar?](nstoolbaritem/toolbar.md)
  The toolbar that currently includes the item.
### Validating the item
- [var autovalidates: Bool](nstoolbaritem/autovalidates.md)
  A Boolean value that indicates whether the toolbar automatically validates the item.
- [func validate()](nstoolbaritem/validate.md)
  Validates the toolbar item’s menu and its ability to perfrom its action.
### Deprecated
- [var allowsDuplicatesInToolbar: Bool](nstoolbaritem/allowsduplicatesintoolbar.md)
  A Boolean value that indicates whether the toolbar item can appear more than once in a toolbar.
- [var minSize: NSSize](nstoolbaritem/minsize.md)
  The toolbar item’s minimum size.
- [var maxSize: NSSize](nstoolbaritem/maxsize.md)
  The toolbar item’s maximum size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMenuToolbarItem](nsmenutoolbaritem.md)
- [NSSearchToolbarItem](nssearchtoolbaritem.md)
- [NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md)
- [NSToolbarItemGroup](nstoolbaritemgroup.md)
- [NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md)
- [Sendable](../Swift/Sendable.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)

## See Also

- [class NSToolbarItemGroup](nstoolbaritemgroup.md)
  A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.
- [class NSMenuToolbarItem](nsmenutoolbaritem.md)
  A control that presents a menu in a window’s toolbar.
- [class NSSearchToolbarItem](nssearchtoolbaritem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.
- [class NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md)
  A toolbar separator that aligns with the vertical split view in the same window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem)*