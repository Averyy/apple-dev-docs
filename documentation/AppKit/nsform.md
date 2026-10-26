# NSForm

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An `NSForm` object is a vertical matrix of [`NSFormCell`](./nsformcell.md) objects to implement the fields.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
class NSForm
```

```objc
@interface NSForm : NSMatrix
```

## Topics

### Adding and Removing Entries
- [func addEntry(String) -> NSFormCell](./nsform/addentry%28_%29.md)
  Adds a new entry to the end of the receiver and gives it the specified title.
- [func insertEntry(String, at: Int) -> NSFormCell!](./nsform/insertentry%28_,at%29.md)
  Inserts an entry with the specified title into the receiver.
- [func removeEntry(at: Int)](./nsform/removeentry%28at%29.md)
  Removes and releases the entry at the specified index.
### Changing the Appearance of All the Entries
- [func setBezeled(Bool)](./nsform/setbezeled%28_%29.md)
  Sets whether the receiver’s entries should display a bezel around their editable text.
- [func setBordered(Bool)](./nsform/setbordered%28_%29.md)
  Sets whether the receiver’s entries should display a border around their editable text fields.
- [func setEntryWidth(CGFloat)](./nsform/setentrywidth%28_%29.md)
  Sets the width of all the entries in the receiver.
- [func setFrameSize(NSSize)](./nsform/setframesize%28_%29.md)
  Sets the size of the receiver’s frame size to the specified value.
- [func setInterlineSpacing(CGFloat)](./nsform/setinterlinespacing%28_%29.md)
  Sets the spacing between entries
- [func setTitleAlignment(NSTextAlignment)](./nsform/settitlealignment%28_%29.md)
  Sets the alignment for all of the entry titles.
- [func setTitleBaseWritingDirection(NSWritingDirection)](./nsform/settitlebasewritingdirection%28_%29.md)
  Sets the writing direction for the title of every control embedded in the form.
- [func setTextAlignment(NSTextAlignment)](./nsform/settextalignment%28_%29.md)
  Sets the alignment for all of the receiver’s editable text.
- [func setTextBaseWritingDirection(NSWritingDirection)](./nsform/settextbasewritingdirection%28_%29.md)
  Sets the writing direction for the text content of every control embedded in the form.
- [func setTitleFont(NSFont)](./nsform/settitlefont%28_%29.md)
  Sets the font for all of the entry titles.
- [func setTextFont(NSFont)](./nsform/settextfont%28_%29.md)
  Sets the font for all of the receiver’s editable text fields
### Getting Cells and Indices
- [func indexOfCell(withTag: Int) -> Int](./nsform/indexofcell%28withtag%29.md)
  Returns the index of the entry whose tag is `tag`.
- [func indexOfSelectedItem() -> Int](./nsform/indexofselecteditem%28%29.md)
  Returns the index of the selected entry.
- [func cell(at: Int) -> Any!](./nsform/cell%28at%29.md)
  Returns the entry at the specified index.
### Displaying a Cell
- [func drawCell(at: Int)](./nsform/drawcell%28at%29.md)
  Displays the entry at the specified index.
### Auto Layout Sizing
- [func preferredTextFieldWidth() -> CGFloat](./nsform/preferredtextfieldwidth%28%29.md)
  The preferred width of the form’s cells when using Auto Layout.
- [func setPreferredTextFieldWidth(CGFloat)](./nsform/setpreferredtextfieldwidth%28_%29.md)
  Sets the preferred text field width used by Auto Layout.
### Editing Text
- [func selectText(at: Int)](./nsform/selecttext%28at%29.md)
  Selects the entry at the specified index.

## Relationships

### Inherits From
- [NSMatrix](./nsmatrix.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](./nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](./nsuserinterfacevalidations.md)
- [NSViewToolTipOwner](./nsviewtooltipowner.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated classes
- [class NSOpenGLView](./nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](./nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](./nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
- [class NSOpenGLPixelFormat](./nsopenglpixelformat.md)
  An object that specifies the types of buffers and other attributes of the OpenGL context.
- [class NSDrawer](./nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSFormCell](./nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](./nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.
- [NSOpenGLPixelBuffer](./nsopenglpixelbuffer.md)
  An object that provides access to accelerated offscreen rendering.
- [NSCachedImageRep](./nscachedimagerep.md)
  An object that stores image data in a form that can be readily transferred to the screen.
- [NSInputManager](./nsinputmanager.md)
- [NSInputServer](./nsinputserver.md)
- [NSMovie](./nsmovie.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform)*