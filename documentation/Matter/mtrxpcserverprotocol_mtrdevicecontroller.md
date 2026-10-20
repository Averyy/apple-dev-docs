# MTRXPCServerProtocol_MTRDeviceController

**Framework**: Matter  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 18.3+
- iPadOS 18.3+
- Mac Catalyst 18.3+
- macOS 15.3+
- tvOS 18.3+
- visionOS 2.3+
- watchOS 11.3+

## Declaration

```swift
protocol MTRXPCServerProtocol_MTRDeviceController : NSObjectProtocol
```

```objc
@protocol MTRXPCServerProtocol_MTRDeviceController <NSObject>
```

## Topics

### Instance Methods
- [func deviceController(UUID, deleteNodeID: NSNumber)](./mtrxpcserverprotocol_mtrdevicecontroller/devicecontroller%28_,deletenodeid%29.md)
- [func deviceController(UUID, getNodesWithStoredDataWithReply: ([NSNumber]) -> Void)](./mtrxpcserverprotocol_mtrdevicecontroller/devicecontroller%28_,getnodeswithstoreddatawithreply%29.md)
- [func deviceController(UUID, registerNodeID: NSNumber)](./mtrxpcserverprotocol_mtrdevicecontroller/devicecontroller%28_,registernodeid%29.md)
- [func deviceController(UUID, unregisterNodeID: NSNumber)](./mtrxpcserverprotocol_mtrdevicecontroller/devicecontroller%28_,unregisternodeid%29.md)
- [func deviceController(UUID, updateControllerConfiguration: [AnyHashable : Any])](./mtrxpcserverprotocol_mtrdevicecontroller/devicecontroller%28_,updatecontrollerconfiguration%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [MTRXPCServerProtocol](./mtrxpcserverprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevicecontroller)*