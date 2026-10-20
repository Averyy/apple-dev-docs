# PGDevice

**Framework**: Paravirtualized Graphics  
**Kind**: protocol  
**Role**: Protocol

A paravirtualized GPU device object.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
protocol PGDevice : NSObjectProtocol
```

```objc
@protocol PGDevice <NSObject>
```

## Topics

### Handling Memory-Mapped I/O
- [func mmioRead(atOffset: Int) -> UInt32](./pgdevice/mmioread%28atoffset%29.md)
  Reads data from the virtual graphics device’s memory-mapped I/O region.
- [func mmioWrite(atOffset: Int, value: UInt32)](./pgdevice/mmiowrite%28atoffset,value%29.md)
  Writes data to the virtual graphics device’s memory-mapped I/O region.
### Suspending and Resuming Graphics Processing
- [func willSuspend()](./pgdevice/willsuspend%28%29.md)
  Notifies the virtual graphics device to start suspending graphics activities.
- [func finishSuspend() -> Data?](./pgdevice/finishsuspend%28%29.md)
  Notifies the virtualized graphics device to finish suspending graphics activities.
- [func willResume(withSuspendState: Data, error: NSErrorPointer) -> Bool](./pgdevice/willresume%28withsuspendstate,error%29.md)
  Tells a new device object to load a previously saved device’s suspend state.
- [func didResume()](./pgdevice/didresume%28%29.md)
  Tells the device object to finish any remaining work to resume processing of a previously saved device’s suspend state.
- [let PGResumeErrorDomain: String](./pgresumeerrordomain.md)
  The error domain for suspend-resume actions.
- [enum PGResumeErrorCode](./pgresumeerrorcode.md)
  Error codes for suspend-resume actions.
### Managing Displays
- [func newDisplay(with: PGDisplayDescriptor, port: Int, serialNum: UInt32) -> (any PGDisplay)?](./pgdevice/newdisplay%28with,port,serialnum%29.md)
  Create a display from the specified descriptor and uniquifying parameters.
### Instance Methods
- [func pause()](./pgdevice/pause%28%29.md)
- [func reset()](./pgdevice/reset%28%29.md)
- [func stop()](./pgdevice/stop%28%29.md)
- [func unpause()](./pgdevice/unpause%28%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Devices
- [class PGDeviceDescriptor](./pgdevicedescriptor.md)
  A description of the paravirtualized graphics device to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice)*