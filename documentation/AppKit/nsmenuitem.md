# NSMenuItem

**Framework**: AppKit  
**Kind**: class

A command item in an app menu.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSMenuItem
```

#### Overview

The [`NSMenuItem`](nsmenuitem.md) class includes some private functionality needed to maintain binary compatibility with other components of Cocoa. Because of this fact, you can’t replace the [`NSMenuItem`](nsmenuitem.md) class with a different class, but you can subclass it if necessary.

## Topics

### Creating a menu item
- [init(title: String, action: Selector?, keyEquivalent: String)](nsmenuitem/init(title:action:keyequivalent:).md)
  Returns an initialized instance of `NSMenuItem`.
- [init(coder: NSCoder)](nsmenuitem/init(coder:).md)
### Enabling a menu item
- [var isEnabled: Bool](nsmenuitem/isenabled.md)
  A Boolean value that indicates whether the menu item is enabled.
### Managing hidden status
- [var isHidden: Bool](nsmenuitem/ishidden.md)
  A Boolean value that indicates whether the menu item is hidden.
- [var isHiddenOrHasHiddenAncestor: Bool](nsmenuitem/ishiddenorhashiddenancestor.md)
  A Boolean value that indicates whether the menu item or any of its superitems is hidden.
### Managing the target and action
- [var target: AnyObject?](nsmenuitem/target.md)
  The menu item’s target.
- [var action: Selector?](nsmenuitem/action.md)
  The menu item’s action-method selector.
### Managing the title
- [var title: String](nsmenuitem/title.md)
  The menu item’s title.
- [var attributedTitle: NSAttributedString?](nsmenuitem/attributedtitle.md)
  A custom string for a menu item.
### Managing the tag
- [var tag: Int](nsmenuitem/tag.md)
  The menu item’s tag.
### Managing the state
- [var state: NSControl.StateValue](nsmenuitem/state.md)
  The state of the menu item.
### Managing the image
- [var image: NSImage?](nsmenuitem/image.md)
  The menu item’s image.
- [var onStateImage: NSImage!](nsmenuitem/onstateimage.md)
  The image of the menu item that indicates an “on” state.
- [var offStateImage: NSImage?](nsmenuitem/offstateimage.md)
  The image of the menu item that indicates an “off” state.
- [var mixedStateImage: NSImage!](nsmenuitem/mixedstateimage.md)
  The image of the menu item that indicates a “mixed” state, that is, a state neither “on” nor “off.”
### Managing the badge
- [var badge: NSMenuItemBadge?](nsmenuitem/badge.md)
### Managing the section header
- [var isSectionHeader: Bool](nsmenuitem/issectionheader.md)
  A Boolean value indicating whether the menu item is a section header.
### Managing submenus
- [var submenu: NSMenu?](nsmenuitem/submenu.md)
  The submenu of the menu item.
- [var hasSubmenu: Bool](nsmenuitem/hassubmenu.md)
  A Boolean value that indicates whether the menu item has a submenu.
- [var parent: NSMenuItem?](nsmenuitem/parent.md)
  The menu item whose submenu contains the receiver.
### Managing the separator item
- [var isSeparatorItem: Bool](nsmenuitem/isseparatoritem.md)
  A Boolean value indicating whether the menu item is a separator item.
- [class func separator() -> NSMenuItem](nsmenuitem/separator.md)
  Returns a menu item that is used to separate logical groups of menu commands.
### Managing the owning menu
- [var menu: NSMenu?](nsmenuitem/menu.md)
  The menu item’s menu.
### Managing key equivalents
- [var keyEquivalent: String](nsmenuitem/keyequivalent.md)
  The menu item’s unmodified key equivalent.
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](nsmenuitem/keyequivalentmodifiermask.md)
  The menu item’s keyboard equivalent modifiers.
### Managing mnemonics
- [func setTitleWithMnemonic(String)](nsmenuitem/settitlewithmnemonic(_:).md)
  Sets the title of a menu item with a character denoting an access key.
### Managing user key equivalents
- [class var usesUserKeyEquivalents: Bool](nsmenuitem/usesuserkeyequivalents.md)
  Returns a Boolean value that indicates whether menu items conform to user preferences for key equivalents.
- [var userKeyEquivalent: String](nsmenuitem/userkeyequivalent.md)
  The user-assigned key equivalent for the menu item.
- [var allowsAutomaticKeyEquivalentLocalization: Bool](nsmenuitem/allowsautomatickeyequivalentlocalization.md)
  A Boolean value that determines whether the system automatically remaps the keyboard shortcut to support localized keyboards.
- [var allowsAutomaticKeyEquivalentMirroring: Bool](nsmenuitem/allowsautomatickeyequivalentmirroring.md)
  A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.
- [var allowsKeyEquivalentWhenHidden: Bool](nsmenuitem/allowskeyequivalentwhenhidden.md)
### Managing alternates
- [var isAlternate: Bool](nsmenuitem/isalternate.md)
  A Boolean value that marks the menu item as an alternate to the previous menu item.
### Managing indentation levels
- [var indentationLevel: Int](nsmenuitem/indentationlevel.md)
  The menu item indentation level for the menu item.
### Managing tool tips
- [var toolTip: String?](nsmenuitem/tooltip.md)
  A help tag for the menu item.
### Representing an object
- [var representedObject: Any?](nsmenuitem/representedobject.md)
  The object represented by the menu item.
### Managing the view
- [var view: NSView?](nsmenuitem/view.md)
  The content view for the menu item.
### Getting highlighted status
- [var isHighlighted: Bool](nsmenuitem/ishighlighted.md)
  A Boolean value that indicates whether the menu item should be drawn highlighted.
### Identifying the Continuity Camera menu item
- [class let importFromDeviceIdentifier: NSUserInterfaceItemIdentifier](nsmenuitem/importfromdeviceidentifier.md)
  The identifier for a Continuity Camera menu item, which takes pictures or scans documents using an iOS device.
### Type Methods
- [static func sectionHeader(title: String) -> NSMenuItem](nsmenuitem/sectionheader(title:).md)
- [static func sectionHeader(withTitle: String) -> NSMenuItem](nsmenuitem/sectionheader(withtitle:).md)
### Instance Properties
- [var subtitle: String?](nsmenuitem/subtitle.md)
### Type Properties
- [class var writingToolsItems: [NSMenuItem]](nsmenuitem/writingtoolsitems.md)
  An array of standard menu items related to Writing Tools. Each call to this method returns an array of newly allocated instances of NSMenuItem.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md)

## See Also

- [class NSMenu](nsmenu.md)
  An object that manages an app’s menus.
- [class NSMenuItemBadge](nsmenuitembadge.md)
  A control that provides additional quantitative information specific to a menu item, such as the number of available updates.
- [protocol NSMenuDelegate](nsmenudelegate.md)
  The optional methods implemented by delegates of [`NSMenu`](nsmenu.md) objects to manage menu display and handle some events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem)*