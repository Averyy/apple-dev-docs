# MTRDevice

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRDevice
```

```objc
@interface MTRDevice : NSObject
```

## Topics

### Initializers
- [init(nodeID: NSNumber, controller: MTRDeviceController)](./mtrdevice/init%28nodeid,controller%29.md)
- [init(nodeID: UInt64, deviceController: MTRDeviceController)](./mtrdevice/init%28nodeid,devicecontroller%29.md)
### Instance Properties
- [var deviceCachePrimed: Bool](./mtrdevice/devicecacheprimed.md)
- [var deviceController: MTRDeviceController?](./mtrdevice/devicecontroller.md)
- [var estimatedStartTime: Date?](./mtrdevice/estimatedstarttime.md)
- [var estimatedSubscriptionLatency: NSNumber?](./mtrdevice/estimatedsubscriptionlatency.md)
- [var state: MTRDeviceState](./mtrdevice/state.md)
- [var networkCommissioningFeatures: MTRNetworkCommissioningFeature](./mtrdevice/networkcommissioningfeatures.md)
  Network commissioning features supported by the device.
- [var productID: NSNumber?](./mtrdevice/productid.md)
  The Product Identifier associated with the device.
- [var vendorID: NSNumber?](./mtrdevice/vendorid.md)
  The Vendor Identifier associated with the device.
### Instance Methods
- [func downloadLog(of: MTRDiagnosticLogType, timeout: TimeInterval, queue: dispatch_queue_t, completion: (URL?, (any Error)?) -> Void)](./mtrdevice/downloadlog%28of,timeout,queue,completion%29.md)
- [func invokeCommand(withEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: [String : Any]?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, queue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](./mtrdevice/invokecommand%28withendpointid,clusterid,commandid,commandfields,expectedvalues,expectedvalueinterval,queue,completion%29.md)
- [func invokeCommand(withEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout: NSNumber?, clientQueue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](./mtrdevice/invokecommand%28withendpointid,clusterid,commandid,commandfields,expectedvalues,expectedvalueinterval,timedinvoketimeout,clientqueue,completion%29.md)
- [func invokeCommand(withEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout: NSNumber?, queue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](./mtrdevice/invokecommand%28withendpointid,clusterid,commandid,commandfields,expectedvalues,expectedvalueinterval,timedinvoketimeout,queue,completion%29.md)
- [func openCommissioningWindow(withDiscriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t, completion: (MTRSetupPayload?, (any Error)?) -> Void)](./mtrdevice/opencommissioningwindow%28withdiscriminator,duration,queue,completion%29.md)
- [func openCommissioningWindow(withSetupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t, completion: (MTRSetupPayload?, (any Error)?) -> Void)](./mtrdevice/opencommissioningwindow%28withsetuppasscode,discriminator,duration,queue,completion%29.md)
- [func readAttribute(withEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, params: MTRReadParams?) -> [String : Any]?](./mtrdevice/readattribute%28withendpointid,clusterid,attributeid,params%29.md)
- [func setDelegate(any MTRDeviceDelegate, queue: dispatch_queue_t)](./mtrdevice/setdelegate%28_,queue%29.md)
- [func writeAttribute(withEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, expectedValueInterval: NSNumber, timedWriteTimeout: NSNumber?)](./mtrdevice/writeattribute%28withendpointid,clusterid,attributeid,value,expectedvalueinterval,timedwritetimeout%29.md)
- [func add(any MTRDeviceDelegate, queue: dispatch_queue_t)](./mtrdevice/add%28_,queue%29.md)
  Adds a delegate to receive asynchronous callbacks about the device.
- [func add(any MTRDeviceDelegate, queue: dispatch_queue_t, interestedPathsForAttributes: [Any]?, interestedPathsForEvents: [Any]?)](./mtrdevice/add%28_,queue,interestedpathsforattributes,interestedpathsforevents%29.md)
  Adds a delegate to receive asynchronous callbacks about the device, and limit attribute and/or event reports to a specific set of paths.
- [func descriptorClusters() -> [MTRAttributePath : [String : Any]]](./mtrdevice/descriptorclusters%28%29.md)
  Read all known attributes from descriptor clusters on all known endpoints.
- [func invokeCommands([[MTRCommandWithRequiredResponse]], queue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](./mtrdevice/invokecommands%28_,queue,completion%29.md)
  Invoke one or more groups of commands.
- [func readAttributePaths([MTRAttributeRequestPath]) -> [[String : Any]]](./mtrdevice/readattributepaths%28_%29.md)
  Read the attributes identified by the provided attribute paths.  The paths can include wildcards.
- [func remove(any MTRDeviceDelegate)](./mtrdevice/remove%28_%29.md)
  Removes the delegate from receiving callbacks about the device.
- [func wait(forAttributeValues: [MTRAttributePath : [String : Any]], timeout: TimeInterval, queue: dispatch_queue_t, completion: ((any Error)?) -> Void) -> MTRAttributeValueWaiter](./mtrdevice/wait%28forattributevalues,timeout,queue,completion%29.md)
  Sets up the provided completion to be called when any of the following happens:

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice)*