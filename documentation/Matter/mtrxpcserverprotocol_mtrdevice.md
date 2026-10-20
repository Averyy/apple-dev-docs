# MTRXPCServerProtocol_MTRDevice

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
protocol MTRXPCServerProtocol_MTRDevice : NSObjectProtocol
```

```objc
@protocol MTRXPCServerProtocol_MTRDevice <NSObject>
```

## Topics

### Instance Methods
- [func deviceController(UUID, nodeID: NSNumber, downloadLogOf: MTRDiagnosticLogType, timeout: TimeInterval, completion: (URL?, (any Error)?) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,downloadlogof,timeout,completion%29.md)
- [func deviceController(UUID, nodeID: NSNumber, getDeviceCachePrimedWithReply: (Bool) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,getdevicecacheprimedwithreply%29.md)
- [func deviceController(UUID, nodeID: NSNumber, getEstimatedStartTimeWithReply: (Date?) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,getestimatedstarttimewithreply%29.md)
- [func deviceController(UUID, nodeID: NSNumber, getEstimatedSubscriptionLatencyWithReply: (NSNumber?) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,getestimatedsubscriptionlatencywithreply%29.md)
- [func deviceController(UUID, nodeID: NSNumber, getStateWithReply: (MTRDeviceState) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,getstatewithreply%29.md)
- [func deviceController(UUID, nodeID: NSNumber, invokeCommandWithEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout: NSNumber?, serverSideProcessingTimeout: NSNumber?, completion: ([[String : Any]]?, (any Error)?) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,invokecommandwithendpointid,clusterid,commandid,commandfields,expectedvalues,expectedvalueinterval,timedinvoketimeout,serversideprocessingtimeout,completion%29.md)
- [func deviceController(UUID, nodeID: NSNumber, invokeCommands: [[MTRCommandWithRequiredResponse]], completion: ([[String : Any]]?, (any Error)?) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,invokecommands,completion%29.md)
- [func deviceController(UUID, nodeID: NSNumber, openCommissioningWindowWithSetupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, completion: (MTRSetupPayload?, (any Error)?) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,opencommissioningwindowwithsetuppasscode,discriminator,duration,completion%29.md)
- [func deviceController(UUID, nodeID: NSNumber, readAttributePaths: [MTRAttributeRequestPath], withReply: ([[String : Any]]) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,readattributepaths,withreply%29.md)
- [func deviceController(UUID, nodeID: NSNumber, readAttributeWithEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, params: MTRReadParams?, withReply: ([String : Any]?) -> Void)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,readattributewithendpointid,clusterid,attributeid,params,withreply%29.md)
- [func deviceController(UUID, nodeID: NSNumber, writeAttributeWithEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, expectedValueInterval: NSNumber?, timedWriteTimeout: NSNumber?)](./mtrxpcserverprotocol_mtrdevice/devicecontroller%28_,nodeid,writeattributewithendpointid,clusterid,attributeid,value,expectedvalueinterval,timedwritetimeout%29.md)
- [func downloadLog(of: MTRDiagnosticLogType, nodeID: NSNumber, timeout: TimeInterval, completion: (URL?, (any Error)?) -> Void)](./mtrxpcserverprotocol_mtrdevice/downloadlog%28of,nodeid,timeout,completion%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [MTRXPCServerProtocol](./mtrxpcserverprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice)*