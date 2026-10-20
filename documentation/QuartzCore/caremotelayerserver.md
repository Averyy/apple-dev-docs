# CARemoteLayerServer

**Framework**: Core Animation  
**Kind**: class  
**Role**: Class

A legacy class for cross-process rendering.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
class CARemoteLayerServer
```

```objc
@interface CARemoteLayerServer : NSObject
```

#### Overview

`CARemoteLaterServer` is a legacy class for cross-process rendering. [`IOSurfaceCreateMachPort(_:)`](../IOSurface/iosurfacecreatemachport%28_%29.md) and [`IOSurfaceCreateXPCObject(_:)`](../IOSurface/iosurfacecreatexpcobject%28_%29.md), available with [`IOSurface`](../IOSurface/iosurface-page.md), offer an improved way to perform cross-process rendering.

## Topics

### Creating a Server
- [var serverPort: mach_port_t](./caremotelayerserver/serverport.md)
  The port number of the server.
### Getting a Server Instance
- [class func shared() -> CARemoteLayerServer](./caremotelayerserver/shared%28%29.md)
  Returns the (singleton) instance of the shared remote layer server.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Remote Display of Layer Content
- [class CARemoteLayerClient](./caremotelayerclient.md)
  A legacy class for cross-process rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caremotelayerserver)*