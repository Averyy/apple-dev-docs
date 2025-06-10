# NSToolbarItem.Identifier

**Framework**: AppKit  
**Kind**: struct

Constants for the standard toolbar items that the system provides.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
struct Identifier
```

#### Overview

If you configure an [`NSToolbarItem`](nstoolbaritem.md) in Interface Builder with one of the standard identifiers, AppKit configures the toolbar item for you automatically when you load your interface. Similarly, if your toolbar delegate returns them as part of the default or allowed set of items, AppKit handles their configuration. When your delegate provides standard identifiers, AppKit doesn’t call the [`toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)`](nstoolbardelegate/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:).md) method for them.

## Topics

### Getting the standard item identifiers
- [static let space: NSToolbarItem.Identifier](nstoolbaritem/identifier/space.md)
  The identifier for a toolbar item that displays an empty space with a standard fixed size.
- [static let flexibleSpace: NSToolbarItem.Identifier](nstoolbaritem/identifier/flexiblespace.md)
  The identifier for a toolbar item that displays an empty space with a flexible width.
- [static let cloudSharing: NSToolbarItem.Identifier](nstoolbaritem/identifier/cloudsharing.md)
  The identifier for a toolbar item that tells your app to display the iCloud sharing interface.
- [static let print: NSToolbarItem.Identifier](nstoolbaritem/identifier/print.md)
  The identifier for a toolbar item that tells your app to print the current document.
- [static let showColors: NSToolbarItem.Identifier](nstoolbaritem/identifier/showcolors.md)
  The identifier for a toolbar item that shows the standard color panel.
- [static let showFonts: NSToolbarItem.Identifier](nstoolbaritem/identifier/showfonts.md)
  The identifier for a toolbar item that shows the standard font panel.
- [static let toggleSidebar: NSToolbarItem.Identifier](nstoolbaritem/identifier/togglesidebar.md)
  The identifier for a toolbar item that displays a sidebar.
- [static let sidebarTrackingSeparator: NSToolbarItem.Identifier](nstoolbaritem/identifier/sidebartrackingseparator.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the sidebar divider in a split view.
- [static let primarySidebarTrackingSeparatorItemIdentifier: NSToolbarItem.Identifier](nstoolbaritem/identifier/primarysidebartrackingseparatoritemidentifier.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the primary divider in a split view.
- [static let supplementarySidebarTrackingSeparatorItemIdentifier: NSToolbarItem.Identifier](nstoolbaritem/identifier/supplementarysidebartrackingseparatoritemidentifier.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the secondary divider in a split view.
- [static let inspectorTrackingSeparator: NSToolbarItem.Identifier](nstoolbaritem/identifier/inspectortrackingseparator.md)
- [static let toggleInspector: NSToolbarItem.Identifier](nstoolbaritem/identifier/toggleinspector.md)
### Creating an identifier
- [init(String)](nstoolbaritem/identifier/init(_:).md)
  Creates a toolbar item identifier.
- [init(rawValue: String)](nstoolbaritem/identifier/init(rawvalue:).md)
  Creates a toolbar item identifier with the specified raw value.
### Deprecated
- [static let customizeToolbar: NSToolbarItem.Identifier](nstoolbaritem/identifier/customizetoolbar.md)
  The Customize item, which shows the customization palette.
- [static let separator: NSToolbarItem.Identifier](nstoolbaritem/identifier/separator.md)
  The Separator item.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var itemIdentifier: NSToolbarItem.Identifier](nstoolbaritem/itemidentifier.md)
  The value you use to identify the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/identifier)*