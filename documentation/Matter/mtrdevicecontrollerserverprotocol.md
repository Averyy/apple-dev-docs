# MTRDeviceControllerServerProtocol

**Framework**: Matter  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MTRDeviceControllerServerProtocol <NSObject>
```

## Topics

### Instance Methods
- [func downloadLog(withController: Any?, nodeId: NSNumber, type: MTRDiagnosticLogType, timeout: TimeInterval, completion: (String?, (any Error)?) -> Void)](./mtrdevicecontrollerserverprotocol/downloadlog%28withcontroller,nodeid,type,timeout,completion%29.md)
- [func getAnyDeviceController(completion: (Any?, (any Error)?) -> Void)](./mtrdevicecontrollerserverprotocol/getanydevicecontroller%28completion%29.md)
- [func getDeviceController(withFabricId: UInt64, completion: (Any?, (any Error)?) -> Void)](./mtrdevicecontrollerserverprotocol/getdevicecontroller%28withfabricid,completion%29.md)
- [func invokeCommand(withController: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber, fields: Any, timedInvokeTimeout: NSNumber?, completion: (Any?, (any Error)?) -> Void)](./mtrdevicecontrollerserverprotocol/invokecommand%28withcontroller,nodeid,endpointid,clusterid,commandid,fields,timedinvoketimeout,completion%29.md)
- [func readAttribute(withController: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, params: [String : Any]?, completion: (Any?, (any Error)?) -> Void)](./mtrdevicecontrollerserverprotocol/readattribute%28withcontroller,nodeid,endpointid,clusterid,attributeid,params,completion%29.md)
- [func readAttributeCache(withController: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, completion: (Any?, (any Error)?) -> Void)](./mtrdevicecontrollerserverprotocol/readattributecache%28withcontroller,nodeid,endpointid,clusterid,attributeid,completion%29.md)
- [func stopReports(withController: Any?, nodeId: UInt64, completion: () -> Void)](./mtrdevicecontrollerserverprotocol/stopreports%28withcontroller,nodeid,completion%29.md)
- [func subscribe(withController: Any?, nodeId: UInt64, minInterval: NSNumber, maxInterval: NSNumber, params: [String : Any]?, shouldCache: Bool, completion: ((any Error)?) -> Void)](./mtrdevicecontrollerserverprotocol/subscribe%28withcontroller,nodeid,mininterval,maxinterval,params,shouldcache,completion%29.md)
- [func subscribeAttribute(withController: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, minInterval: NSNumber, maxInterval: NSNumber, params: [String : Any]?, establishedHandler: () -> Void)](./mtrdevicecontrollerserverprotocol/subscribeattribute%28withcontroller,nodeid,endpointid,clusterid,attributeid,mininterval,maxinterval,params,establishedhandler%29.md)
- [func writeAttribute(withController: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, attributeId: NSNumber, value: Any, timedWriteTimeout: NSNumber?, completion: (Any?, (any Error)?) -> Void)](./mtrdevicecontrollerserverprotocol/writeattribute%28withcontroller,nodeid,endpointid,clusterid,attributeid,value,timedwritetimeout,completion%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol)*