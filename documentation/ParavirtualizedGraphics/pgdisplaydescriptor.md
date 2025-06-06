# PGDisplayDescriptor

**Framework**: Paravirtualized Graphics  
**Kind**: class

A descriptor for a virtual display.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class PGDisplayDescriptor
```

## Topics

### Specifying the Display Properties
- [var name: String?](pgdisplaydescriptor/name.md)
  The display’s name as seen in the guest operating environment.
- [var sizeInMillimeters: NSSize](pgdisplaydescriptor/sizeinmillimeters.md)
  The size in millimeters of the virtual display.
### Setting the Dispatch Queue
- [var queue: dispatch_queue_t?](pgdisplaydescriptor/queue.md)
  The queue that the framework uses when dispatching messages to any of the display’s registered handlers.
### Managing Cursor Events
- [var cursorGlyphHandler: PGDisplayCursorGlyphHandler?](pgdisplaydescriptor/cursorglyphhandler.md)
  A handler that the framework calls to change the cursor’s appearance.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](pgdisplaydescriptor/cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [typealias PGDisplayCursorGlyphHandler](pgdisplaycursorglyphhandler.md)
  The block signature for a routine that handles changes to the cursor’s appearance.
- [typealias PGDisplayCursorShowHandler](pgdisplaycursorshowhandler.md)
  The block signature for a routine that handles changes to the cursor’s visibility.
### Handling Mode Changes
- [var modeChangeHandler: PGDisplayModeChangeHandler?](pgdisplaydescriptor/modechangehandler.md)
  A handler that the framework calls to change the virtual display’s graphics mode.
- [typealias PGDisplayModeChangeHandler](pgdisplaymodechangehandler.md)
  The block signature for a routine that handles changes to the display’s graphics mode.
### Handling Frame Events
- [var newFrameEventHandler: PGDisplayNewFrameEventHandler?](pgdisplaydescriptor/newframeeventhandler.md)
  A handler that the framework calls when the guest environment has a new frame to display.
- [typealias PGDisplayNewFrameEventHandler](pgdisplaynewframeeventhandler.md)
  The block signature for a routine that handles frame updates from the guest.
### Instance Properties
- [var cursorMoveHandler: PGDisplayCursorMoveHandler?](pgdisplaydescriptor/cursormovehandler.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol PGDisplay](pgdisplay.md)
  An object that provides display functionality to the guest operating system in a way that the host-side virtual machine app can intercept.
- [class PGDisplayMode](pgdisplaymode.md)
  A description of a supported display mode.
- [struct PGDisplayCoord_t](pgdisplaycoord_t.md)
  Coordinates that describe sizes or offsets within a 2D array of pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor)*