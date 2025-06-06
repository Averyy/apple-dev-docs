# MTRXPCServerProtocol_MTRDevice

**Framework**: Matter  
**Kind**: protocol

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

## Topics

### Instance Methods
- [func deviceController(UUID, nodeID: NSNumber, downloadLogOf: MTRDiagnosticLogType, timeout: TimeInterval, completion: (URL?, (any Error)?) -> Void)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:downloadlogof:timeout:completion:).md)
- [func deviceController(UUID, nodeID: NSNumber, getDeviceCachePrimedWithReply: (Bool) -> Void)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:getdevicecacheprimedwithreply:).md)
- [func deviceController(UUID, nodeID: NSNumber, getEstimatedStartTimeWithReply: (Date?) -> Void)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:getestimatedstarttimewithreply:).md)
- [func deviceController(UUID, nodeID: NSNumber, getEstimatedSubscriptionLatencyWithReply: (NSNumber?) -> Void)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:getestimatedsubscriptionlatencywithreply:).md)
- [func deviceController(UUID, nodeID: NSNumber, getStateWithReply: (MTRDeviceState) -> Void)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:getstatewithreply:).md)
- [func deviceController(UUID, nodeID: NSNumber, invokeCommandWithEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout: NSNumber?, serverSideProcessingTimeout: NSNumber?, completion: MTRDeviceResponseHandler)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:invokecommandwithendpointid:clusterid:commandid:commandfields:expectedvalues:expectedvalueinterval:timedinvoketimeout:serversideprocessingtimeout:completion:).md)
- [func deviceController(UUID, nodeID: NSNumber, invokeCommands: [[MTRCommandWithRequiredResponse]], completion: MTRDeviceResponseHandler)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:invokecommands:completion:).md)
- [func deviceController(UUID, nodeID: NSNumber, openCommissioningWindowWithSetupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, completion: MTRDeviceOpenCommissioningWindowHandler)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:opencommissioningwindowwithsetuppasscode:discriminator:duration:completion:).md)
- [func deviceController(UUID, nodeID: NSNumber, readAttributePaths: [MTRAttributeRequestPath], withReply: ([[String : Any]]) -> Void)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:readattributepaths:withreply:).md)
- [func deviceController(UUID, nodeID: NSNumber, readAttributeWithEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, params: MTRReadParams?, withReply: ([String : Any]?) -> Void)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:readattributewithendpointid:clusterid:attributeid:params:withreply:).md)
- [func deviceController(UUID, nodeID: NSNumber, writeAttributeWithEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, expectedValueInterval: NSNumber?, timedWriteTimeout: NSNumber?)](mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:writeattributewithendpointid:clusterid:attributeid:value:expectedvalueinterval:timedwritetimeout:).md)
- [func downloadLog(of: MTRDiagnosticLogType, nodeID: NSNumber, timeout: TimeInterval, completion: (URL?, (any Error)?) -> Void)](mtrxpcserverprotocol_mtrdevice/downloadlog(of:nodeid:timeout:completion:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTRXPCServerProtocol](mtrxpcserverprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice)*