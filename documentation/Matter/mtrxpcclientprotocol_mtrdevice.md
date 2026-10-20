# MTRXPCClientProtocol_MTRDevice

**Framework**: Matter  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
protocol MTRXPCClientProtocol_MTRDevice : NSObjectProtocol
```

```objc
@protocol MTRXPCClientProtocol_MTRDevice <NSObject>
```

## Topics

### Instance Methods
- [func device(NSNumber, internalStateUpdated: [AnyHashable : Any])](./mtrxpcclientprotocol_mtrdevice/device%28_,internalstateupdated%29.md)
- [func device(NSNumber, receivedAttributeReport: [[String : Any]])](./mtrxpcclientprotocol_mtrdevice/device%28_,receivedattributereport%29.md)
- [func device(NSNumber, receivedEventReport: [[String : Any]])](./mtrxpcclientprotocol_mtrdevice/device%28_,receivedeventreport%29.md)
- [func device(NSNumber, stateChanged: MTRDeviceState)](./mtrxpcclientprotocol_mtrdevice/device%28_,statechanged%29.md)
- [func deviceBecameActive(NSNumber)](./mtrxpcclientprotocol_mtrdevice/devicebecameactive%28_%29.md)
- [func deviceCachePrimed(NSNumber)](./mtrxpcclientprotocol_mtrdevice/devicecacheprimed%28_%29.md)
- [func deviceConfigurationChanged(NSNumber)](./mtrxpcclientprotocol_mtrdevice/deviceconfigurationchanged%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [MTRXPCClientProtocol](./mtrxpcclientprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcclientprotocol_mtrdevice)*