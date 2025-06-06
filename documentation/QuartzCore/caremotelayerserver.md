# CARemoteLayerServer

**Framework**: Core Animation  
**Kind**: class

A legacy class for cross-process rendering.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
class CARemoteLayerServer
```

#### Overview

`CARemoteLaterServer` is a legacy class for cross-process rendering. [`IOSurfaceCreateMachPort(_:)`](https://developer.apple.com/documentation/IOSurface/IOSurfaceCreateMachPort(_:)) and [`IOSurfaceCreateXPCObject(_:)`](https://developer.apple.com/documentation/IOSurface/IOSurfaceCreateXPCObject(_:)), available with [`IOSurface`](https://developer.apple.com/documentation/IOSurface/IOSurface), offer an improved way to perform cross-process rendering.

## Topics

### Creating a Server
- [var serverPort: mach_port_t](caremotelayerserver/serverport.md)
  The port number of the server.
### Getting a Server Instance
- [class func shared() -> CARemoteLayerServer](caremotelayerserver/shared.md)
  Returns the (singleton) instance of the shared remote layer server.

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

- [class CARemoteLayerClient](caremotelayerclient.md)
  A legacy class for cross-process rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caremotelayerserver)*