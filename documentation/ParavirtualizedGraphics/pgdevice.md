# PGDevice

**Framework**: Paravirtualized Graphics  
**Kind**: protocol

A paravirtualized GPU device object.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
protocol PGDevice : NSObjectProtocol
```

## Topics

### Handling Memory-Mapped I/O
- [func mmioRead(atOffset: Int) -> UInt32](pgdevice/mmioread(atoffset:).md)
  Reads data from the virtual graphics device’s memory-mapped I/O region.
- [func mmioWrite(atOffset: Int, value: UInt32)](pgdevice/mmiowrite(atoffset:value:).md)
  Writes data to the virtual graphics device’s memory-mapped I/O region.
### Suspending and Resuming Graphics Processing
- [func willSuspend()](pgdevice/willsuspend.md)
  Notifies the virtual graphics device to start suspending graphics activities.
- [func finishSuspend() -> Data?](pgdevice/finishsuspend.md)
  Notifies the virtualized graphics device to finish suspending graphics activities.
- [func willResume(withSuspendState: Data, error: NSErrorPointer) -> Bool](pgdevice/willresume(withsuspendstate:error:).md)
  Tells a new device object to load a previously saved device’s suspend state.
- [func didResume()](pgdevice/didresume.md)
  Tells the device object to finish any remaining work to resume processing of a previously saved device’s suspend state.
- [let PGResumeErrorDomain: String](pgresumeerrordomain.md)
  The error domain for suspend-resume actions.
- [enum PGResumeErrorCode](pgresumeerrorcode.md)
  Error codes for suspend-resume actions.
### Managing Displays
- [func newDisplay(with: PGDisplayDescriptor, port: Int, serialNum: UInt32) -> (any PGDisplay)?](pgdevice/newdisplay(with:port:serialnum:).md)
  Create a display from the specified descriptor and uniquifying parameters.
### Instance Methods
- [func pause()](pgdevice/pause.md)
- [func reset()](pgdevice/reset.md)
- [func stop()](pgdevice/stop.md)
- [func unpause()](pgdevice/unpause.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func PGNewDeviceWithDescriptor(PGDeviceDescriptor) -> (any PGDevice)?](pgnewdevicewithdescriptor(_:).md)
  Creates a new paravirtualized graphics device.
- [class PGDeviceDescriptor](pgdevicedescriptor.md)
  A description of the paravirtualized graphics device to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice)*