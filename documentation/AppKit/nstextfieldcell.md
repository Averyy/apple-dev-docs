# NSTextFieldCell

**Framework**: AppKit  
**Kind**: class

An object that enhances the text display capabilities of a cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTextFieldCell
```

#### Overview

The [`NSTextFieldCell`](nstextfieldcell.md) class adds to the text display capabilities of the [`NSCell`](nscell.md) class by allowing you to set the color of both the text and its background. You can also specify whether the cell draws its background at all.

All of the methods declared by this class are also declared by the [`NSTextField`](nstextfield.md) class, which uses [`NSTextFieldCell`](nstextfieldcell.md) objects to draw and edit text. The [`NSTextField`](nstextfield.md) cover methods call the corresponding [`NSTextFieldCell`](nstextfieldcell.md) methods.

Placeholder strings, set using the [`placeholderString`](nstextfieldcell/placeholderstring.md) or [`placeholderAttributedString`](nstextfieldcell/placeholderattributedstring.md) property, appear in the text field cell if the actual string is `nil` or an empty string. They’re drawn in gray on the cell and aren’t archived in the “pre-10.2” nib format.

##### Designated Initializers

When subclassing `NSTextFieldCell` you must implement the designated initializers [`init(coder:)`](nscell/init(coder:).md) and [`init(textCell:)`](nscell/init(textcell:).md).

## Topics

### Creating a Text Field Cell
- [init(textCell: String)](nstextfieldcell/init(textcell:).md)
  Initializes a text field cell that displays the specified string.
- [init(coder: NSCoder)](nstextfieldcell/init(coder:).md)
  Initializes a text field cell from data in the provided unarchiver.
### Setting the Text Color
- [var textColor: NSColor?](nstextfieldcell/textcolor.md)
  The color to use to draw the cell’s text.
### Setting the Bezel Style
- [var bezelStyle: NSTextField.BezelStyle](nstextfieldcell/bezelstyle.md)
  The bezel style to use when drawing the text field.
- [NSTextField.BezelStyle](nstextfield/bezelstyle-swift.enum.md)
  The style of bezel the text field displays.
### Controlling the Background
- [var backgroundColor: NSColor?](nstextfieldcell/backgroundcolor.md)
  The color of the cell’s background.
- [var drawsBackground: Bool](nstextfieldcell/drawsbackground.md)
  A Boolean value that indicates whether the cell draws its background color.
### Managing the Field Editor
- [func setUpFieldEditorAttributes(NSText) -> NSText](nstextfieldcell/setupfieldeditorattributes(_:).md)
  Allows the cell to set up the field editor’s attributes before editing begins.
- [func setWantsNotificationForMarkedText(Bool)](nstextfieldcell/setwantsnotificationformarkedtext(_:).md)
  Directs the cell’s associated field editor to post text change notifications.
### Managing Placeholder Strings
- [var placeholderString: String?](nstextfieldcell/placeholderstring.md)
  The placeholder text for the cell, specified as a plain text string.
- [var placeholderAttributedString: NSAttributedString?](nstextfieldcell/placeholderattributedstring.md)
  The placeholder text for the cell, specified as an attributed string.
### Accessing Input Source Locales
- [var allowedInputSourceLocales: [String]?](nstextfieldcell/allowedinputsourcelocales.md)
  An array of locale identifiers that represent the allowed input sources when the text field has the keyboard focus.

## Relationships

### Inherits From
- [NSActionCell](nsactioncell.md)
### Inherited By
- [NSComboBoxCell](nscomboboxcell.md)
- [NSPathComponentCell](nspathcomponentcell.md)
- [NSSearchFieldCell](nssearchfieldcell.md)
- [NSSecureTextFieldCell](nssecuretextfieldcell.md)
- [NSTableHeaderCell](nstableheadercell.md)
- [NSTokenFieldCell](nstokenfieldcell.md)
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

## See Also

- [class NSSecureTextFieldCell](nssecuretextfieldcell.md)
  A text field whose value is hidden from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell)*