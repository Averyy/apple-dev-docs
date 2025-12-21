# NSDrawer

**Framework**: AppKit  
**Kind**: class

A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class NSDrawer
```

#### Overview

A drawer is associated with a window, called its parent, and can appear only while its parent is visible onscreen. A drawer cannot be moved or ordered independently of a window, but is instead attached to one edge of its parent and moves along with it.

## Topics

### Creating Drawers
- [init(contentSize: NSSize, preferredEdge: NSRectEdge)](nsdrawer/init(contentsize:preferrededge:).md)
  Creates a new drawer with the given size on the specified edge of the parent window.
- [var delegate: (any NSDrawerDelegate)?](nsdrawer/delegate.md)
  The receiver’s delegate.
### Opening and Closing Drawers
- [func close()](nsdrawer/close.md)
  If the receiver is open, this method closes it.
- [func close(Any?)](nsdrawer/close(_:).md)
  An action method to close the receiver.
- [func open()](nsdrawer/open.md)
  If the receiver is closed, this method opens it.
- [func open(Any?)](nsdrawer/open(_:).md)
  An action method to open the drawer.
- [func open(on: NSRectEdge)](nsdrawer/open(on:).md)
  Causes the receiver to open on the specified edge of the parent window.
- [func toggle(Any?)](nsdrawer/toggle(_:).md)
  Toggles the drawer open or closed.
- [var state: Int](nsdrawer/state-swift.property.md)
  The state of the receiver.
### Managing Drawer Size
- [var contentSize: NSSize](nsdrawer/contentsize.md)
  The size of the receiver’s content area.
- [var leadingOffset: CGFloat](nsdrawer/leadingoffset.md)
  The receiver’s leading offset.
- [var maxContentSize: NSSize](nsdrawer/maxcontentsize.md)
  The maximum allowed size of the receiver’s content area.
- [var minContentSize: NSSize](nsdrawer/mincontentsize.md)
  The minimum allowed size of the receiver’s content area.
- [var trailingOffset: CGFloat](nsdrawer/trailingoffset.md)
  The receiver’s trailing offset.
### Managing Drawer Edges
- [var edge: NSRectEdge](nsdrawer/edge.md)
  The edge of the window that the receiver is connected to.
- [var preferredEdge: NSRectEdge](nsdrawer/preferrededge.md)
  The receiver’s preferred, or default, edge.
### Managing Drawer Views
- [var contentView: NSView?](nsdrawer/contentview.md)
  The receiver’s content view.
- [var parentWindow: NSWindow?](nsdrawer/parentwindow.md)
  The receiver’s parent window.
### Constants
- [NSDrawer.State](nsdrawer/state-swift.enum.md)
  These constants specify the possible states of a drawer.
### Notifications
- [class let didCloseNotification: NSNotification.Name](nsdrawer/didclosenotification.md)
  Posted whenever the drawer is closed.
- [class let didOpenNotification: NSNotification.Name](nsdrawer/didopennotification.md)
  Posted whenever the drawer is opened.
- [class let willCloseNotification: NSNotification.Name](nsdrawer/willclosenotification.md)
  Posted whenever the drawer is about to close.
- [class let willOpenNotification: NSNotification.Name](nsdrawer/willopennotification.md)
  Posted whenever the drawer is about to open.

## Relationships

### Inherits From
- [NSResponder](nsresponder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
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
- [class NSForm](nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](nsformcell.md) objects to implement the fields.
- [class NSFormCell](nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer)*