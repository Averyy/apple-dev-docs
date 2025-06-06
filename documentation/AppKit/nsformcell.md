# NSFormCell

**Framework**: AppKit  
**Kind**: class

The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSFormCell
```

#### Overview

An `NSFormCell` object implements the user interface of an [`NSForm`](nsform.md) object.

## Topics

### Initializers
- [init(coder: NSCoder)](nsformcell/init(coder:).md)
### Initializing an NSFormCell
- [init(textCell: String?)](nsformcell/init(textcell:).md)
  Returns an `NSFormCell` object initialized with the specified title string.
### Asking About a Cell’s Appearance
- [var isOpaque: Bool](nsformcell/isopaque.md)
  A Boolean value indicating whether the title is empty and an opaque bezel is set.
### Accessing a Cell’s Title
- [var attributedTitle: NSAttributedString](nsformcell/attributedtitle.md)
  The title of the cell as an attributed string.
- [var title: String](nsformcell/title.md)
  The cell’s title text.
- [var titleAlignment: NSTextAlignment](nsformcell/titlealignment.md)
  The alignment of the title.
- [var titleBaseWritingDirection: NSWritingDirection](nsformcell/titlebasewritingdirection.md)
  The default writing direction used to render the form cell’s title.
- [var titleFont: NSFont](nsformcell/titlefont.md)
  The font used to draw cell’s title.
- [var titleWidth: CGFloat](nsformcell/titlewidth.md)
  The width of the title field.
### Asking About Placeholder Values
- [var placeholderAttributedString: NSAttributedString?](nsformcell/placeholderattributedstring.md)
  The cell’s attributed placeholder string.
- [var placeholderString: String?](nsformcell/placeholderstring.md)
  The cell’s plain text placeholder string.
### Sizing for Auto Layout
- [var preferredTextFieldWidth: CGFloat](nsformcell/preferredtextfieldwidth.md)
  The preferred text field width.
### Instance Methods
- [func titleWidth(NSSize) -> CGFloat](nsformcell/titlewidth(_:).md)
  Returns the width of the title field constrained to the specified size.

## Relationships

### Inherits From
- [NSActionCell](nsactioncell.md)
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
- [class NSForm](nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](nsformcell.md) objects to implement the fields.
- [class NSMenuItemCell](nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell)*