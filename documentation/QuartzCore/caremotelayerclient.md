# CARemoteLayerClient

**Framework**: Core Animation  
**Kind**: class  
**Role**: Class

A legacy class for cross-process rendering.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
class CARemoteLayerClient
```

```objc
@interface CARemoteLayerClient : NSObject
```

#### Overview

`CARemoteLaterClient` is a legacy class for cross-process rendering. [`IOSurfaceCreateMachPort(_:)`](../IOSurface/iosurfacecreatemachport%28_%29.md) and [`IOSurfaceCreateXPCObject(_:)`](../IOSurface/iosurfacecreatexpcobject%28_%29.md), available with [`IOSurface`](../IOSurface/iosurface-page.md), offer an improved way to perform cross-process rendering.

## Topics

### Creating a Client
- [init(serverPort: mach_port_t)](./caremotelayerclient/init%28serverport%29.md)
  Creates a layer client from a server port.
### Retrieving Client Properties
- [var clientId: UInt32](./caremotelayerclient/clientid.md)
  The ID of the remote layer client.
- [var layer: CALayer?](./caremotelayerclient/layer.md)
  The layer associated with the remote client.
### Invalidating a Client
- [func invalidate()](./caremotelayerclient/invalidate%28%29.md)
  Invalidates a remote layer client.

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
- [class CARemoteLayerServer](./caremotelayerserver.md)
  A legacy class for cross-process rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caremotelayerclient)*