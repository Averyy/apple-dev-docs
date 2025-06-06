# CARemoteLayerClient

**Framework**: Core Animation  
**Kind**: class

A legacy class for cross-process rendering.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
class CARemoteLayerClient
```

#### Overview

`CARemoteLaterClient` is a legacy class for cross-process rendering. [`IOSurfaceCreateMachPort(_:)`](https://developer.apple.com/documentation/IOSurface/IOSurfaceCreateMachPort(_:)) and [`IOSurfaceCreateXPCObject(_:)`](https://developer.apple.com/documentation/IOSurface/IOSurfaceCreateXPCObject(_:)), available with [`IOSurface`](https://developer.apple.com/documentation/IOSurface/IOSurface), offer an improved way to perform cross-process rendering.

## Topics

### Creating a Client
- [init(serverPort: mach_port_t)](caremotelayerclient/init(serverport:).md)
  Creates a layer client from a server port.
### Retrieving Client Properties
- [var clientId: UInt32](caremotelayerclient/clientid.md)
  The ID of the remote layer client.
- [var layer: CALayer?](caremotelayerclient/layer.md)
  The layer associated with the remote client.
### Invalidating a Client
- [func invalidate()](caremotelayerclient/invalidate.md)
  Invalidates a remote layer client.

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

- [class CARemoteLayerServer](caremotelayerserver.md)
  A legacy class for cross-process rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caremotelayerclient)*