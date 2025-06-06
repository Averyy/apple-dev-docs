# PGDisplay

**Framework**: Paravirtualized Graphics  
**Kind**: protocol

An object that provides display functionality to the guest operating system in a way that the host-side virtual machine app can intercept.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
protocol PGDisplay : NSObjectProtocol
```

#### Overview

The framework emulates hot-plugging to the display. After you create the display object, set the [`modeList`](pgdisplay/modelist.md) property to a list of modes you want the display to use. The first time you set the mode list, the framework connects the display to the virtualized graphics card. When you release the display object, the device simulates unplugging the display.

## Topics

### Setting Display Modes
- [var modeList: [PGDisplayMode]](pgdisplay/modelist.md)
  The list of display modes that the virtual display supports.
### Getting the Guest Cursor Position
- [var cursorPosition: PGDisplayCoord_t](pgdisplay/cursorposition.md)
  The current cursor location in the guest environment.
### Handling Frame Updates
- [var guestPresentCount: Int](pgdisplay/guestpresentcount.md)
  The number of frame presents that the guest has generated since object creation.
- [var hostPresentCount: Int](pgdisplay/hostpresentcount.md)
  The number of unique frames that the host has encoded since object creation.
- [var minimumTextureUsage: MTLTextureUsage](pgdisplay/minimumtextureusage.md)
  The Metal texture usage flags necessary for any texture that can be a destination for frame data.
- [func encodeCurrentFrame(to: any MTLCommandBuffer, texture: any MTLTexture, region: MTLRegion) -> Bool](pgdisplay/encodecurrentframe(to:texture:region:).md)
  Encodes Metal commands to process the current frame and write it to a texture.
### Inspecting Display Properties
- [var name: String?](pgdisplay/name.md)
  The display’s name that you specified at creation time.
- [var serialNum: UInt32](pgdisplay/serialnum.md)
  The display’s serial number that you specified at creation time.
- [var port: Int](pgdisplay/port.md)
  The display’s accelerator port that you specified at creation time.
- [var sizeInMillimeters: NSSize](pgdisplay/sizeinmillimeters.md)
  The display’s virtual dimensions, in millimeters, that you specified at creation time.
### Inspecting the Display Handlers
- [var queue: dispatch_queue_t?](pgdisplay/queue.md)
  The queue that the framework uses when dispatching messages to any of the display’s registered handlers.
- [var cursorGlyphHandler: PGDisplayCursorGlyphHandler?](pgdisplay/cursorglyphhandler.md)
  A handler that the framework calls to change the cursor’s appearance.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](pgdisplay/cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [var modeChangeHandler: PGDisplayModeChangeHandler?](pgdisplay/modechangehandler.md)
  A handler that the framework calls to change the virtual display’s graphics mode.
- [var newFrameEventHandler: PGDisplayNewFrameEventHandler?](pgdisplay/newframeeventhandler.md)
  A handler that the framework calls when the guest environment has a new frame to display.
### Instance Properties
- [var cursorMoveHandler: PGDisplayCursorMoveHandler?](pgdisplay/cursormovehandler.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PGDisplayDescriptor](pgdisplaydescriptor.md)
  A descriptor for a virtual display.
- [class PGDisplayMode](pgdisplaymode.md)
  A description of a supported display mode.
- [struct PGDisplayCoord_t](pgdisplaycoord_t.md)
  Coordinates that describe sizes or offsets within a 2D array of pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay)*