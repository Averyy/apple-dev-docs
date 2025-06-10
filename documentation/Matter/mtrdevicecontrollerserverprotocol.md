# MTRDeviceControllerServerProtocol

**Framework**: Matter  
**Kind**: protocol

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol MTRDeviceControllerServerProtocol : NSObjectProtocol
```

## Topics

### Instance Methods
- [func downloadLog(withController: Any?, nodeId: NSNumber, type: MTRDiagnosticLogType, timeout: TimeInterval, completion: (String?, (any Error)?) -> Void)](mtrdevicecontrollerserverprotocol/downloadlog(withcontroller:nodeid:type:timeout:completion:).md)
- [func getAnyDeviceController(completion: (Any?, (any Error)?) -> Void)](mtrdevicecontrollerserverprotocol/getanydevicecontroller(completion:).md)
- [func getDeviceController(withFabricId: UInt64, completion: (Any?, (any Error)?) -> Void)](mtrdevicecontrollerserverprotocol/getdevicecontroller(withfabricid:completion:).md)
- [func invokeCommand(withController: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber, fields: Any, timedInvokeTimeout: NSNumber?, completion: (Any?, (any Error)?) -> Void)](mtrdevicecontrollerserverprotocol/invokecommand(withcontroller:nodeid:endpointid:clusterid:commandid:fields:timedinvoketimeout:completion:).md)
- [func readAttribute(withController: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, params: [String : Any]?, completion: (Any?, (any Error)?) -> Void)](mtrdevicecontrollerserverprotocol/readattribute(withcontroller:nodeid:endpointid:clusterid:attributeid:params:completion:).md)
- [func readAttributeCache(withController: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, completion: (Any?, (any Error)?) -> Void)](mtrdevicecontrollerserverprotocol/readattributecache(withcontroller:nodeid:endpointid:clusterid:attributeid:completion:).md)
- [func stopReports(withController: Any?, nodeId: UInt64, completion: () -> Void)](mtrdevicecontrollerserverprotocol/stopreports(withcontroller:nodeid:completion:).md)
- [func subscribe(withController: Any?, nodeId: UInt64, minInterval: NSNumber, maxInterval: NSNumber, params: [String : Any]?, shouldCache: Bool, completion: ((any Error)?) -> Void)](mtrdevicecontrollerserverprotocol/subscribe(withcontroller:nodeid:mininterval:maxinterval:params:shouldcache:completion:).md)
- [func subscribeAttribute(withController: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, minInterval: NSNumber, maxInterval: NSNumber, params: [String : Any]?, establishedHandler: () -> Void)](mtrdevicecontrollerserverprotocol/subscribeattribute(withcontroller:nodeid:endpointid:clusterid:attributeid:mininterval:maxinterval:params:establishedhandler:).md)
- [func writeAttribute(withController: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, attributeId: NSNumber, value: Any, timedWriteTimeout: NSNumber?, completion: (Any?, (any Error)?) -> Void)](mtrdevicecontrollerserverprotocol/writeattribute(withcontroller:nodeid:endpointid:clusterid:attributeid:value:timedwritetimeout:completion:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol)*