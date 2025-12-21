# NSMenuItemCell

**Framework**: AppKit  
**Kind**: class

An object that handles the measurement and display of a single menu item in its encompassing frame.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSMenuItemCell
```

#### Overview

> **Note**:  `NSMenuItemCell` is no longer used to draw menus. Using it does not affect the appearance of your menus.

## Topics

### Initializers
- [init(coder: NSCoder)](nsmenuitemcell/init(coder:).md)
- [init(textCell: String)](nsmenuitemcell/init(textcell:).md)
### Configuring Menu-Item Attributes
- [var menuItem: NSMenuItem?](nsmenuitemcell/menuitem.md)
  The menu item object associated with the cell.
### Calculating the Size of a Menu Item
- [func calcSize()](nsmenuitemcell/calcsize.md)
  Calculates the minimum required width and height of the receiver’s menu item.
- [var needsSizing: Bool](nsmenuitemcell/needssizing.md)
  A Boolean value indicating whether the size of the menu needs to be calculated.
- [var imageWidth: CGFloat](nsmenuitemcell/imagewidth.md)
  The width of the image associated with the menu item.
- [var titleWidth: CGFloat](nsmenuitemcell/titlewidth.md)
  The width of the menu item’s text, measured in points.
- [var keyEquivalentWidth: CGFloat](nsmenuitemcell/keyequivalentwidth.md)
  The width of the menu item’s key equivalent string.
- [var stateImageWidth: CGFloat](nsmenuitemcell/stateimagewidth.md)
  The width of the image used to indicate the state of the menu item.
### Getting the Menu Item’s Drawing Rectangle
- [func keyEquivalentRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/keyequivalentrect(forbounds:).md)
  Returns the rectangle into which the menu item’s key equivalent should be drawn.
- [func stateImageRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/stateimagerect(forbounds:).md)
  Returns the rectangle into which the menu item’s state image should be drawn.
- [func titleRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/titlerect(forbounds:).md)
  Returns the rectangle into which the menu item’s title should be drawn.
### Drawing the Menu Item
- [func drawBorderAndBackground(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawborderandbackground(withframe:in:).md)
  Draws the borders and background associated with the receiver’s menu item (if any).
- [func drawImage(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawimage(withframe:in:).md)
  Draws the image associated with the menu item.
- [func drawKeyEquivalent(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawkeyequivalent(withframe:in:).md)
  Draws the key equivalent associated with the menu item.
- [func drawSeparatorItem(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawseparatoritem(withframe:in:).md)
  Draws a menu item separator.
- [func drawStateImage(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawstateimage(withframe:in:).md)
  Draws the state image associated with the menu item.
- [func drawTitle(withFrame: NSRect, in: NSView)](nsmenuitemcell/drawtitle(withframe:in:).md)
  Draws the title associated with the menu item.
- [var needsDisplay: Bool](nsmenuitemcell/needsdisplay.md)
  A Boolean value indicating whether the menu item needs to be displayed.
### Assigning a Tag
- [var tag: Int](nsmenuitemcell/tag.md)
  The integer tag of the selected menu item.

## Relationships

### Inherits From
- [NSButtonCell](nsbuttoncell.md)
### Inherited By
- [NSPopUpButtonCell](nspopupbuttoncell.md)
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

- [class NSOpenGLView](nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
- [class NSOpenGLPixelFormat](nsopenglpixelformat.md)
  An object that specifies the types of buffers and other attributes of the OpenGL context.
- [class NSDrawer](nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSForm](nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](nsformcell.md) objects to implement the fields.
- [class NSFormCell](nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell)*