# NSSearchField

**Framework**: AppKit  
**Kind**: class

A text field optimized for performing text-based searches.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSSearchField
```

#### Overview

[`NSSearchField`](nssearchfield.md) provides a customized text field for entering search data. The class also provides a search button, a cancel button, and a pop-up icon menu for listing recent search strings and custom search categories.

An [`NSSearchField`](nssearchfield.md) object wraps an [`NSSearchFieldCell`](nssearchfieldcell.md) object. The cell provides access to most search field attributes and a comprehensive programmatic interface for manipulating the search field. You can use an [`NSSearchField`](nssearchfield.md) object to manipulate some aspects of the search field.

For additional information about search fields and how to implement them, see the [`NSSearchFieldCell`](nssearchfieldcell.md) class.

## Topics

### Managing Search
- [var delegate: (any NSSearchFieldDelegate)?](nssearchfield/delegate.md)
  The delegate for the search field, or `nil` if the search field doesn’t have a delegate.
- [protocol NSSearchFieldDelegate](nssearchfielddelegate.md)
  A protocol that a search field delegate can use to determine when a search started or ended.
### Managing Menu Templates
- [var searchMenuTemplate: NSMenu?](nssearchfield/searchmenutemplate.md)
  The menu object used to dynamically construct the search field’s pop-up icon menu.
- [class let clearRecentsMenuItemTag: Int](nssearchfield/clearrecentsmenuitemtag.md)
  The menu item for clearing the current set of recent string searches in the menu.
- [class let noRecentsMenuItemTag: Int](nssearchfield/norecentsmenuitemtag.md)
  The menu item that describes a lack of recent search strings.
- [class let recentsMenuItemTag: Int](nssearchfield/recentsmenuitemtag.md)
  The location of recent search strings in the “recents” menu group.
- [class let recentsTitleMenuItemTag: Int](nssearchfield/recentstitlemenuitemtag.md)
  The menu item that provides the title of the menu group for recent search strings.
### Managing Search Modes
- [var sendsSearchStringImmediately: Bool](nssearchfield/sendssearchstringimmediately.md)
  A Boolean value indicating whether the cell calls its action method immediately when an appropriate action occurs.
- [var sendsWholeSearchString: Bool](nssearchfield/sendswholesearchstring.md)
  A Boolean value indicating whether the cell calls its search action method when the user clicks the search button or presses Return, or after each keystroke.
### Managing Recent Searches
- [var recentSearches: [String]](nssearchfield/recentsearches.md)
  The list of recent search strings for the control.
- [var maximumRecents: Int](nssearchfield/maximumrecents.md)
  The maximum number of search strings that can appear in the search menu.
- [var recentsAutosaveName: NSSearchField.RecentsAutosaveName?](nssearchfield/recentsautosavename-swift.property.md)
  The name under which the search field automatically archives the list of recent search strings.
- [NSSearchField.RecentsAutosaveName](nssearchfield/recentsautosavename-swift.typealias.md)
  The string that stores the name under which a search field automatically archives a list of recent search strings.
### Getting Search Field Metrics
- [var cancelButtonBounds: NSRect](nssearchfield/cancelbuttonbounds.md)
  The rectangle for the cancel button within the bounds of the search field.
- [var searchButtonBounds: NSRect](nssearchfield/searchbuttonbounds.md)
  The rectangle for the search button within the bounds of the search field.
- [var searchTextBounds: NSRect](nssearchfield/searchtextbounds.md)
  The rectangle for the search text within the bounds of the search field.
### Deprecated Symbols
- [var centersPlaceholder: Bool](nssearchfield/centersplaceholder.md)
  A Boolean value that determines whether the search field’s components are centered within the control.
- [func rectForCancelButton(whenCentered: Bool) -> NSRect](nssearchfield/rectforcancelbutton(whencentered:).md)
  The rectangle for the cancel button within the bounds of the search field.
- [func rectForSearchButton(whenCentered: Bool) -> NSRect](nssearchfield/rectforsearchbutton(whencentered:).md)
  The rectangle for the search button within the bounds of the search field.
- [func rectForSearchText(whenCentered: Bool) -> NSRect](nssearchfield/rectforsearchtext(whencentered:).md)
  The rectangle for the search text within the bounds of the field.

## Relationships

### Inherits From
- [NSTextField](nstextfield.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilityStaticText](nsaccessibilitystatictext.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTextContent](nstextcontent.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield)*