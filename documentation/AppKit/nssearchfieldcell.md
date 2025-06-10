# NSSearchFieldCell

**Framework**: AppKit  
**Kind**: class

The programmatic interface for text fields that are used for text-based searches.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSSearchFieldCell
```

#### Overview

The [`NSSearchFieldCell`](nssearchfieldcell.md) class defines the programmatic interface for text fields that are optimized for text-based searches. An [`NSSearchFieldCell`](nssearchfieldcell.md) object is “wrapped” by an [`NSSearchField`](nssearchfield.md) control object, which directly inherits from the [`NSTextField`](nstextfield.md) class. The search field implemented by these classes presents a standard user interface for searches, including a search button, a cancel button, and a pop-up icon menu for listing recent search strings and custom search categories.

When the user types and then pauses, the cell’s action message is sent to its target. You can query the cell’s string value for the current text to search for. Do not rely on the sender of the action to be an [`NSMenu`](nsmenu.md) object because the menu may change. If you need to change the menu, modify the search menu template and update the value in the [`searchMenuTemplate`](nssearchfieldcell/searchmenutemplate.md) property.

## Topics

### Managing buttons
- [var searchButtonCell: NSButtonCell?](nssearchfieldcell/searchbuttoncell.md)
  The button cell used to display the search-button image.
- [func resetSearchButtonCell()](nssearchfieldcell/resetsearchbuttoncell.md)
  Resets the search button cell to its default attributes.
- [var cancelButtonCell: NSButtonCell?](nssearchfieldcell/cancelbuttoncell.md)
  The button cell used to display the cancel-button image.
- [func resetCancelButtonCell()](nssearchfieldcell/resetcancelbuttoncell.md)
  Resets the cancel button cell to its default attributes.
### Custom layout
- [func searchTextRect(forBounds: NSRect) -> NSRect](nssearchfieldcell/searchtextrect(forbounds:).md)
  Modifies the bounding rectangle for the search-text field cell.
- [func searchButtonRect(forBounds: NSRect) -> NSRect](nssearchfieldcell/searchbuttonrect(forbounds:).md)
  Modifies the bounding rectangle for the search button cell.
- [func cancelButtonRect(forBounds: NSRect) -> NSRect](nssearchfieldcell/cancelbuttonrect(forbounds:).md)
  Modifies the bounding rectangle for the cancel button cell.
### Managing menu templates
- [var searchMenuTemplate: NSMenu?](nssearchfieldcell/searchmenutemplate.md)
  The menu object used to dynamically construct the search field’s pop-up icon menu.
### Managing search modes
- [var sendsWholeSearchString: Bool](nssearchfieldcell/sendswholesearchstring.md)
  A Boolean value indicating whether the cell calls its search action method when the user clicks the search button (or presses Return) or after each keystroke.
- [var sendsSearchStringImmediately: Bool](nssearchfieldcell/sendssearchstringimmediately.md)
  A Boolean value indicating whether the cell calls its action method immediately when an appropriate action occurs.
### Managing recent search strings
- [var maximumRecents: Int](nssearchfieldcell/maximumrecents.md)
  The maximum number of search strings that can appear in the search menu.
- [var recentSearches: [String]!](nssearchfieldcell/recentsearches.md)
  An array of the recent search strings to display in the pop-up icon menu of the search field.
- [var recentsAutosaveName: NSSearchField.RecentsAutosaveName?](nssearchfieldcell/recentsautosavename.md)
  The autosave name under which the search field automatically saves the list of recent search strings.
### Constants
- [Menu tags](menu-tags.md)
  Constants for identifying special menu items in the search-menu template.
### Initializers
- [init(coder: NSCoder)](nssearchfieldcell/init(coder:).md)
- [init(textCell: String)](nssearchfieldcell/init(textcell:).md)

## Relationships

### Inherits From
- [NSTextFieldCell](nstextfieldcell.md)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell)*