# NSForm

**Framework**: AppKit  
**Kind**: class

An `NSForm` object is a vertical matrix of [`NSFormCell`](nsformcell.md) objects to implement the fields.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class NSForm
```

## Topics

### Adding and Removing Entries
- [func addEntry(String) -> NSFormCell](nsform/addentry(_:).md)
  Adds a new entry to the end of the receiver and gives it the specified title.
- [func insertEntry(String, at: Int) -> NSFormCell!](nsform/insertentry(_:at:).md)
  Inserts an entry with the specified title into the receiver.
- [func removeEntry(at: Int)](nsform/removeentry(at:).md)
  Removes and releases the entry at the specified index.
### Changing the Appearance of All the Entries
- [func setBezeled(Bool)](nsform/setbezeled(_:).md)
  Sets whether the receiver’s entries should display a bezel around their editable text.
- [func setBordered(Bool)](nsform/setbordered(_:).md)
  Sets whether the receiver’s entries should display a border around their editable text fields.
- [func setEntryWidth(CGFloat)](nsform/setentrywidth(_:).md)
  Sets the width of all the entries in the receiver.
- [func setFrameSize(NSSize)](nsform/setframesize(_:).md)
  Sets the size of the receiver’s frame size to the specified value.
- [func setInterlineSpacing(CGFloat)](nsform/setinterlinespacing(_:).md)
  Sets the spacing between entries
- [func setTitleAlignment(NSTextAlignment)](nsform/settitlealignment(_:).md)
  Sets the alignment for all of the entry titles.
- [func setTitleBaseWritingDirection(NSWritingDirection)](nsform/settitlebasewritingdirection(_:).md)
  Sets the writing direction for the title of every control embedded in the form.
- [func setTextAlignment(NSTextAlignment)](nsform/settextalignment(_:).md)
  Sets the alignment for all of the receiver’s editable text.
- [func setTextBaseWritingDirection(NSWritingDirection)](nsform/settextbasewritingdirection(_:).md)
  Sets the writing direction for the text content of every control embedded in the form.
- [func setTitleFont(NSFont)](nsform/settitlefont(_:).md)
  Sets the font for all of the entry titles.
- [func setTextFont(NSFont)](nsform/settextfont(_:).md)
  Sets the font for all of the receiver’s editable text fields
### Getting Cells and Indices
- [func indexOfCell(withTag: Int) -> Int](nsform/indexofcell(withtag:).md)
  Returns the index of the entry whose tag is `tag`.
- [func indexOfSelectedItem() -> Int](nsform/indexofselecteditem.md)
  Returns the index of the selected entry.
- [func cell(at: Int) -> Any!](nsform/cell(at:).md)
  Returns the entry at the specified index.
### Displaying a Cell
- [func drawCell(at: Int)](nsform/drawcell(at:).md)
  Displays the entry at the specified index.
### Auto Layout Sizing
- [func preferredTextFieldWidth() -> CGFloat](nsform/preferredtextfieldwidth.md)
  The preferred width of the form’s cells when using Auto Layout.
- [func setPreferredTextFieldWidth(CGFloat)](nsform/setpreferredtextfieldwidth(_:).md)
  Sets the preferred text field width used by Auto Layout.
### Editing Text
- [func selectText(at: Int)](nsform/selecttext(at:).md)
  Selects the entry at the specified index.

## Relationships

### Inherits From
- [NSMatrix](nsmatrix.md)
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
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [NSViewToolTipOwner](nsviewtooltipowner.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSOpenGLView](nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](nsopengllayer.md)
  A subclass of [`CAOpenGLLayer`](https://developer.apple.com/documentation/QuartzCore/CAOpenGLLayer) that is suitable for rendering OpenGL into layers.
- [class NSOpenGLPixelFormat](nsopenglpixelformat.md)
  An object that specifies the types of buffers and other attributes of the OpenGL context.
- [class NSDrawer](nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSFormCell](nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform)*