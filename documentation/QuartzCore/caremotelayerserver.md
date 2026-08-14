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

`CARemoteLaterServer` is a legacy class for cross-process rendering. [`IOSurfaceCreateMachPort(_:)`](https://developer.apple.com/documentation/iosurface/iosurfacecreatemachport(_:)) and [`IOSurfaceCreateXPCObject(_:)`](https://developer.apple.com/documentation/iosurface/iosurfacecreatexpcobject(_:)), available with [`IOSurface`](https://developer.apple.com/documentation/iosurface/iosurface), offer an improved way to perform cross-process rendering.

## Topics

### Creating a Server
- [var serverPort: mach_port_t](caremotelayerserver/serverport.md)
  The port number of the server.
### Getting a Server Instance
- [class func shared() -> CARemoteLayerServer](caremotelayerserver/shared.md)
  Returns the (singleton) instance of the shared remote layer server.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CARemoteLayerClient](caremotelayerclient.md)
  A legacy class for cross-process rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caremotelayerserver)*