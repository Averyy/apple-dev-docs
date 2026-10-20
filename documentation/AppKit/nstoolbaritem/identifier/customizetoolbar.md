# customizeToolbar

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The Customize item, which shows the customization palette.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: In macOS 10.7 and later, the customization icon is removed from the toolbar and customization palettes. The system ignores this constant.

## Declaration

```swift
static let customizeToolbar: NSToolbarItem.Identifier
```

```c
extern NSToolbarItemIdentifier NSToolbarCustomizeToolbarItemIdentifier;
```

## See Also

### Getting the standard item identifiers
- [static let space: NSToolbarItem.Identifier](./space.md)
  The identifier for a toolbar item that displays an empty space with a standard fixed size.
- [static let flexibleSpace: NSToolbarItem.Identifier](./flexiblespace.md)
  The identifier for a toolbar item that displays an empty space with a flexible width.
- [static let cloudSharing: NSToolbarItem.Identifier](./cloudsharing.md)
  The identifier for a toolbar item that tells your app to display the iCloud sharing interface.
- [static let print: NSToolbarItem.Identifier](./print.md)
  The identifier for a toolbar item that tells your app to print the current document.
- [static let showColors: NSToolbarItem.Identifier](./showcolors.md)
  The identifier for a toolbar item that shows the standard color panel.
- [static let showFonts: NSToolbarItem.Identifier](./showfonts.md)
  The identifier for a toolbar item that shows the standard font panel.
- [static let toggleSidebar: NSToolbarItem.Identifier](./togglesidebar.md)
  The identifier for a toolbar item that displays a sidebar.
- [static let sidebarTrackingSeparator: NSToolbarItem.Identifier](./sidebartrackingseparator.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the sidebar divider in a split view.
- [static let primarySidebarTrackingSeparatorItemIdentifier: NSToolbarItem.Identifier](./primarysidebartrackingseparatoritemidentifier.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the primary divider in a split view.
- [static let supplementarySidebarTrackingSeparatorItemIdentifier: NSToolbarItem.Identifier](./supplementarysidebartrackingseparatoritemidentifier.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the secondary divider in a split view.
- [static let inspectorTrackingSeparator: NSToolbarItem.Identifier](./inspectortrackingseparator.md)
  Creates a new `NSTrackingSeparatorToolbarItem` and automatically configures it to track the divider of the inspector if one is discovered.
- [static let toggleInspector: NSToolbarItem.Identifier](./toggleinspector.md)
  The identifier for a toolbar item that displays an inspector.
- [static let separator: NSToolbarItem.Identifier](./separator.md)
  The Separator item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/identifier/customizetoolbar)*