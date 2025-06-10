# NSText

**Framework**: AppKit  
**Kind**: class

The most general programmatic interface for objects that manage text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSText
```

#### Overview

[`NSText`](nstext.md) draws text for user interface objects, provides text editing capabilities, and controls text attributes such as type size, font, and color.

[`NSText`](nstext.md) initialization creates an instance of a concrete subclass, such as [`NSTextView`](nstextview.md) (generically called a text object). In general, you’re more likely to use the [`NSTextView`](nstextview.md) subclass, because it extends the interface declared by [`NSText`](nstext.md) and provides much more sophisticated functionality than that declared in [`NSText`](nstext.md).

AppKit uses text objects wherever text appears in interface objects. For example, a text object draws the title of a window, the commands in a menu, the title of a button, and the items in a browser. Your app can also create text objects for its own purposes.

## Topics

### Creating a Text Object
- [init?(coder: NSCoder)](nstext/init(coder:).md)
- [init(frame: NSRect)](nstext/init(frame:).md)
### Getting the characters
- [var string: String](nstext/string.md)
  The characters of the receiver’s text.
### Setting graphics attributes
- [var backgroundColor: NSColor?](nstext/backgroundcolor.md)
  The receiver’s background color to a given color.
- [var drawsBackground: Bool](nstext/drawsbackground.md)
  A Boolean that controls whether the receiver draws its background.
### Setting behavioral attributes
- [var isEditable: Bool](nstext/iseditable.md)
  A Boolean that controls whether the receiver allows the user to edit its text.
- [var isSelectable: Bool](nstext/isselectable.md)
  A Boolean that controls whether the receiver allows the user to select its text.
- [var isFieldEditor: Bool](nstext/isfieldeditor.md)
  A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.
- [var isRichText: Bool](nstext/isrichtext.md)
  A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.
- [var importsGraphics: Bool](nstext/importsgraphics.md)
  A Boolean that controls whether the receiver allows the user to import files by dragging.
### Using the Font panel and menu
- [var usesFontPanel: Bool](nstext/usesfontpanel.md)
  A Boolean that controls whether the receiver uses the Font panel and Font menu.
### Using the ruler
- [func toggleRuler(Any?)](nstext/toggleruler(_:).md)
  This action method shows or hides the ruler, if the receiver is enclosed in a scroll view.
- [var isRulerVisible: Bool](nstext/isrulervisible.md)
  A Boolean value that indicates whether the receiver’s enclosing scroll view shows its ruler.
### Changing the selection
- [var selectedRange: NSRange](nstext/selectedrange.md)
  The receiver’s characters within `aRange`.
### Replacing text
- [func replaceCharacters(in: NSRange, withRTF: Data)](nstext/replacecharacters(in:withrtf:).md)
  Replaces the characters in the given range with RTF text interpreted from the given RTF data.
- [func replaceCharacters(in: NSRange, withRTFD: Data)](nstext/replacecharacters(in:withrtfd:).md)
  Replaces the characters in the given range with RTFD text interpreted from the given RTFD data.
- [func replaceCharacters(in: NSRange, with: String)](nstext/replacecharacters(in:with:).md)
  Replaces the characters in the given range with those in the given string.
### Action methods for editing
- [func selectAll(Any?)](nstext/selectall(_:).md)
  This action method selects all of the receiver’s text.
- [func copy(Any?)](nstext/copy(_:).md)
  This action method copies the selected text onto the general pasteboard, in as many formats as the receiver supports.
- [func cut(Any?)](nstext/cut(_:).md)
  This action method deletes the selected text and places it onto the general pasteboard, in as many formats as the receiver supports.
- [func paste(Any?)](nstext/paste(_:).md)
  This action method pastes text from the general pasteboard at the insertion point or over the selection.
- [func copyFont(Any?)](nstext/copyfont(_:).md)
  This action method copies the font information for the first character of the selection (or for the insertion point) onto the font pasteboard, as `NSFontPboardType`.
- [func pasteFont(Any?)](nstext/pastefont(_:).md)
  This action method pastes font information from the font pasteboard onto the selected text or insertion point of a rich text object, or over all text of a plain text object.
- [func copyRuler(Any?)](nstext/copyruler(_:).md)
  This action method copies the paragraph style information for first selected paragraph onto the ruler pasteboard, as `NSRulerPboardType`, and expands the selection to paragraph boundaries.
- [func pasteRuler(Any?)](nstext/pasteruler(_:).md)
  This action method pastes paragraph style information from the ruler pasteboard onto the selected paragraphs of a rich text object.
- [func delete(Any?)](nstext/delete(_:).md)
  This action method deletes the selected text.
### Changing the font
- [func changeFont(Any?)](nstext/changefont(_:).md)
  This action method changes the font of the selection for a rich text object, or of all text for a plain text object.
- [var font: NSFont?](nstext/font.md)
  The font of all the receiver’s text.
- [func setFont(NSFont, range: NSRange)](nstext/setfont(_:range:).md)
  Sets the font of characters within `aRange` to `aFont`.
### Setting text alignment
- [var alignment: NSTextAlignment](nstext/alignment.md)
  The alignment of all the receiver’s text.
- [func alignCenter(Any?)](nstext/aligncenter(_:).md)
  This action method applies center alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [func alignLeft(Any?)](nstext/alignleft(_:).md)
  This action method applies left alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [func alignRight(Any?)](nstext/alignright(_:).md)
  This action method applies right alignment to selected paragraphs (or all text if the receiver is a plain text object).
### Setting text color
- [var textColor: NSColor?](nstext/textcolor.md)
  The text color of all characters in the receiver.
- [func setTextColor(NSColor?, range: NSRange)](nstext/settextcolor(_:range:).md)
  Sets the text color of characters within the specified range to the specified color.
### Writing direction
- [var baseWritingDirection: NSWritingDirection](nstext/basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.
### Setting superscripting and subscripting
- [func superscript(Any?)](nstext/superscript(_:).md)
  This action method applies a superscript attribute to selected text (or all text if the receiver is a plain text object), raising its baseline offset by a predefined amount.
- [func `subscript`(Any?)](nstext/subscript(_:).md)
  This action method applies a subscript attribute to selected text (or all text if the receiver is a plain text object), lowering its baseline offset by a predefined amount.
- [func unscript(Any?)](nstext/unscript(_:).md)
  This action method removes any superscripting or subscripting from selected text (or all text if the receiver is a plain text object).
### Underlining text
- [func underline(Any?)](nstext/underline(_:).md)
  Adds the underline attribute to the selected text attributes if absent; removes the attribute if present.
### Reading and writing RTF files
- [func readRTFD(fromFile: String) -> Bool](nstext/readrtfd(fromfile:).md)
  Attempts to read the RTFD file at `path`, returning [`true`](https://developer.apple.com/documentation/swift/true) if successful and [`false`](https://developer.apple.com/documentation/swift/false) if not.
- [func writeRTFD(toFile: String, atomically: Bool) -> Bool](nstext/writertfd(tofile:atomically:).md)
  Writes the receiver’s text as RTF with attachments to a file or directory at `path`.
- [func rtfd(from: NSRange) -> Data?](nstext/rtfd(from:).md)
  Returns an NSData object that contains an RTFD stream corresponding to the characters and attributes within `aRange`.
- [func rtf(from: NSRange) -> Data?](nstext/rtf(from:).md)
  Returns an NSData object that contains an RTF stream corresponding to the characters and attributes within `aRange`, omitting any attachment characters and attributes.
### Checking spelling
- [func checkSpelling(Any?)](nstext/checkspelling(_:).md)
  This action method searches for a misspelled word in the receiver’s text.
- [func showGuessPanel(Any?)](nstext/showguesspanel(_:).md)
  This action method opens the Spelling panel, allowing the user to make a correction during spell checking.
### Constraining size
- [var maxSize: NSSize](nstext/maxsize.md)
  The receiver’s maximum size.
- [var minSize: NSSize](nstext/minsize.md)
  The receiver’s minimum size.
- [var isVerticallyResizable: Bool](nstext/isverticallyresizable.md)
  A Boolean that controls whether the receiver changes its height to fit the height of its text.
- [var isHorizontallyResizable: Bool](nstext/ishorizontallyresizable.md)
  A Boolean that controls whether the receiver changes its width to fit the width of its text.
- [func sizeToFit()](nstext/sizetofit.md)
  Resizes the receiver to fit its text.
### Scrolling
- [func scrollRangeToVisible(NSRange)](nstext/scrollrangetovisible(_:).md)
  Scrolls the receiver in its enclosing scroll view so the first characters of `aRange` are visible.
### Setting the delegate
- [var delegate: (any NSTextDelegate)?](nstext/delegate.md)
  The receiver’s delegate.
### Constants
- [enum NSTextAlignment](nstextalignment.md)
  Constants that specify text alignment.
- [enum NSWritingDirection](nswritingdirection.md)
  Constants that specify the writing direction.
- [Movement Codes](movement-codes.md)
  The reason for a change of editing focus among text fields.
- [Common Unicode Characters](common-unicode-characters.md)
### Notifications
- [class let didBeginEditingNotification: NSNotification.Name](nstext/didbegineditingnotification.md)
  Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [class let didChangeNotification: NSNotification.Name](nstext/didchangenotification.md)
  Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [class let didEndEditingNotification: NSNotification.Name](nstext/didendeditingnotification.md)
  Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.
- [class let movementUserInfoKey: String](nstext/movementuserinfokey.md)
  The `userInfo` dictionary key for the [`didEndEditingNotification`](nstext/didendeditingnotification.md) notification.
- [enum NSTextMovement](nstextmovement.md)

## Relationships

### Inherits From
- [NSView](nsview.md)
### Inherited By
- [NSTextView](nstextview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSChangeSpelling](nschangespelling.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSIgnoreMisspelledWords](nsignoremisspelledwords.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSTextField](nstextfield.md)
  Text the user can select or edit to send an action message to a target when the user presses the Return key.
- [protocol NSTextFieldDelegate](nstextfielddelegate.md)
  A protocol that a text field delegate can use to control its field editor action menu.
- [class NSTextView](nstextview.md)
  A view that draws text and handles user interactions with that text.
- [protocol NSTextViewDelegate](nstextviewdelegate.md)
  A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.
- [protocol NSTextDelegate](nstextdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSText`](nstext.md) object to edit text and change text formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext)*