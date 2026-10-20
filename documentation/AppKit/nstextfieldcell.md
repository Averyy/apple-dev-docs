# NSTextFieldCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that enhances the text display capabilities of a cell.

**Availability**:
- macOS

## Declaration

```swift
class NSTextFieldCell
```

```objc
@interface NSTextFieldCell : NSActionCell
```

#### Overview

The [`NSTextFieldCell`](./nstextfieldcell.md) class adds to the text display capabilities of the [`NSCell`](./nscell.md) class by allowing you to set the color of both the text and its background. You can also specify whether the cell draws its background at all.

All of the methods declared by this class are also declared by the [`NSTextField`](./nstextfield.md) class, which uses [`NSTextFieldCell`](./nstextfieldcell.md) objects to draw and edit text. The [`NSTextField`](./nstextfield.md) cover methods call the corresponding [`NSTextFieldCell`](./nstextfieldcell.md) methods.

Placeholder strings, set using the [`placeholderString`](./nstextfieldcell/placeholderstring.md) or [`placeholderAttributedString`](./nstextfieldcell/placeholderattributedstring.md) property, appear in the text field cell if the actual string is `nil` or an empty string. They’re drawn in gray on the cell and aren’t archived in the “pre-10.2” nib format.

##### Designated Initializers

When subclassing `NSTextFieldCell` you must implement the designated initializers [`init(coder:)`](./nscell/init%28coder%29.md) and [`init(textCell:)`](./nscell/init%28textcell%29.md).

## Topics

### Creating a Text Field Cell
- [init(textCell: String)](./nstextfieldcell/init%28textcell%29.md)
  Initializes a text field cell that displays the specified string.
- [init(coder: NSCoder)](./nstextfieldcell/init%28coder%29.md)
  Initializes a text field cell from data in the provided unarchiver.
### Setting the Text Color
- [var textColor: NSColor?](./nstextfieldcell/textcolor.md)
  The color to use to draw the cell’s text.
### Setting the Bezel Style
- [var bezelStyle: NSTextField.BezelStyle](./nstextfieldcell/bezelstyle.md)
  The bezel style to use when drawing the text field.
- [NSTextField.BezelStyle](./nstextfield/bezelstyle-swift.enum.md)
  The style of bezel the text field displays.
### Controlling the Background
- [var backgroundColor: NSColor?](./nstextfieldcell/backgroundcolor.md)
  The color of the cell’s background.
- [var drawsBackground: Bool](./nstextfieldcell/drawsbackground.md)
  A Boolean value that indicates whether the cell draws its background color.
### Managing the Field Editor
- [func setUpFieldEditorAttributes(NSText) -> NSText](./nstextfieldcell/setupfieldeditorattributes%28_%29.md)
  Allows the cell to set up the field editor’s attributes before editing begins.
- [func setWantsNotificationForMarkedText(Bool)](./nstextfieldcell/setwantsnotificationformarkedtext%28_%29.md)
  Directs the cell’s associated field editor to post text change notifications.
### Managing Placeholder Strings
- [var placeholderString: String?](./nstextfieldcell/placeholderstring.md)
  The placeholder text for the cell, specified as a plain text string.
- [var placeholderAttributedString: NSAttributedString?](./nstextfieldcell/placeholderattributedstring.md)
  The placeholder text for the cell, specified as an attributed string.
### Accessing Input Source Locales
- [var allowedInputSourceLocales: [String]?](./nstextfieldcell/allowedinputsourcelocales.md)
  An array of locale identifiers that represent the allowed input sources when the text field has the keyboard focus.

## Relationships

### Inherits From
- [NSActionCell](./nsactioncell.md)
### Inherited By
- [NSComboBoxCell](./nscomboboxcell.md)
- [NSPathComponentCell](./nspathcomponentcell.md)
- [NSSearchFieldCell](./nssearchfieldcell.md)
- [NSSecureTextFieldCell](./nssecuretextfieldcell.md)
- [NSTableHeaderCell](./nstableheadercell.md)
- [NSTokenFieldCell](./nstokenfieldcell.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Cell
- [class NSSecureTextFieldCell](./nssecuretextfieldcell.md)
  A text field whose value is hidden from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell)*