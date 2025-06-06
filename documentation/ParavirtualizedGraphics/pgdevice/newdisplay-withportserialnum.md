# newDisplay(with:port:serialNum:)

**Framework**: Paravirtualized Graphics  
**Kind**: method  
**Required**: Yes

Create a display from the specified descriptor and uniquifying parameters.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func newDisplay(with descriptor: PGDisplayDescriptor, port: Int, serialNum: UInt32) -> (any PGDisplay)?
```

#### Return Value

A new display object, or `nil` if an error occurred.

## Parameters

- `descriptor`: The description of the new display.
- `port`: The port number on the accelerator for the device to use for the new display. Specify a unique port number for each display.
- `serialNum`: A number that uniquely identifies the display. Ensure that the display persists across multiple launches so that the guest compositor can maintain a consistent display layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice/newdisplay(with:port:serialnum:))*