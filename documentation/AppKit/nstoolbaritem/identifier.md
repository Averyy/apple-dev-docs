# NSToolbarItem.Identifier

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants for the standard toolbar items that the system provides.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
struct Identifier
```

```c
typedef NSString * NSToolbarItemIdentifier;
```

#### Overview

If you configure an [`NSToolbarItem`](../nstoolbaritem.md) in Interface Builder with one of the standard identifiers, AppKit configures the toolbar item for you automatically when you load your interface. Similarly, if your toolbar delegate returns them as part of the default or allowed set of items, AppKit handles their configuration. When your delegate provides standard identifiers, AppKit doesn’t call the [`toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)`](../nstoolbardelegate/toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md) method for them.

## Topics

### Getting the standard item identifiers
- [static let space: NSToolbarItem.Identifier](./identifier/space.md)
  The identifier for a toolbar item that displays an empty space with a standard fixed size.
- [static let flexibleSpace: NSToolbarItem.Identifier](./identifier/flexiblespace.md)
  The identifier for a toolbar item that displays an empty space with a flexible width.
- [static let cloudSharing: NSToolbarItem.Identifier](./identifier/cloudsharing.md)
  The identifier for a toolbar item that tells your app to display the iCloud sharing interface.
- [static let print: NSToolbarItem.Identifier](./identifier/print.md)
  The identifier for a toolbar item that tells your app to print the current document.
- [static let showColors: NSToolbarItem.Identifier](./identifier/showcolors.md)
  The identifier for a toolbar item that shows the standard color panel.
- [static let showFonts: NSToolbarItem.Identifier](./identifier/showfonts.md)
  The identifier for a toolbar item that shows the standard font panel.
- [static let toggleSidebar: NSToolbarItem.Identifier](./identifier/togglesidebar.md)
  The identifier for a toolbar item that displays a sidebar.
- [static let sidebarTrackingSeparator: NSToolbarItem.Identifier](./identifier/sidebartrackingseparator.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the sidebar divider in a split view.
- [static let primarySidebarTrackingSeparatorItemIdentifier: NSToolbarItem.Identifier](./identifier/primarysidebartrackingseparatoritemidentifier.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the primary divider in a split view.
- [static let supplementarySidebarTrackingSeparatorItemIdentifier: NSToolbarItem.Identifier](./identifier/supplementarysidebartrackingseparatoritemidentifier.md)
  The identifier for a toolbar item that displays a tracking separator aligned with the secondary divider in a split view.
- [static let inspectorTrackingSeparator: NSToolbarItem.Identifier](./identifier/inspectortrackingseparator.md)
  Creates a new `NSTrackingSeparatorToolbarItem` and automatically configures it to track the divider of the inspector if one is discovered.
- [static let toggleInspector: NSToolbarItem.Identifier](./identifier/toggleinspector.md)
  The identifier for a toolbar item that displays an inspector.
- [static let customizeToolbar: NSToolbarItem.Identifier](./identifier/customizetoolbar.md)
  The Customize item, which shows the customization palette.
- [static let separator: NSToolbarItem.Identifier](./identifier/separator.md)
  The Separator item.
### Creating an identifier
- [init(String)](./identifier/init%28_%29.md)
  Creates a toolbar item identifier.
- [init(rawValue: String)](./identifier/init%28rawvalue%29.md)
  Creates a toolbar item identifier with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the toolbar item’s identity
- [var itemIdentifier: NSToolbarItem.Identifier](./itemidentifier.md)
  The value you use to identify the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/identifier)*