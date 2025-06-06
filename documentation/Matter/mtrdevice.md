# MTRDevice

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init(nodeID: NSNumber, controller: MTRDeviceController)](mtrdevice/init(nodeid:controller:).md)
- [init(nodeID: UInt64, deviceController: MTRDeviceController)](mtrdevice/init(nodeid:devicecontroller:).md)
### Instance Properties
- [var deviceCachePrimed: Bool](mtrdevice/devicecacheprimed.md)
- [var deviceController: MTRDeviceController?](mtrdevice/devicecontroller.md)
- [var estimatedStartTime: Date?](mtrdevice/estimatedstarttime.md)
- [var estimatedSubscriptionLatency: NSNumber?](mtrdevice/estimatedsubscriptionlatency.md)
- [var state: MTRDeviceState](mtrdevice/state.md)
- [var networkCommissioningFeatures: MTRNetworkCommissioningFeature](mtrdevice/networkcommissioningfeatures.md)
  Network commissioning features supported by the device.
- [var productID: NSNumber?](mtrdevice/productid.md)
  The Product Identifier associated with the device.
- [var vendorID: NSNumber?](mtrdevice/vendorid.md)
  The Vendor Identifier associated with the device.
### Instance Methods
- [func downloadLog(of: MTRDiagnosticLogType, timeout: TimeInterval, queue: dispatch_queue_t, completion: (URL?, (any Error)?) -> Void)](mtrdevice/downloadlog(of:timeout:queue:completion:).md)
- [func invokeCommand(withEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: [String : Any]?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, queue: dispatch_queue_t, completion: MTRDeviceResponseHandler)](mtrdevice/invokecommand(withendpointid:clusterid:commandid:commandfields:expectedvalues:expectedvalueinterval:queue:completion:).md)
- [func invokeCommand(withEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout: NSNumber?, clientQueue: dispatch_queue_t, completion: MTRDeviceResponseHandler)](mtrdevice/invokecommand(withendpointid:clusterid:commandid:commandfields:expectedvalues:expectedvalueinterval:timedinvoketimeout:clientqueue:completion:).md)
- [func invokeCommand(withEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout: NSNumber?, queue: dispatch_queue_t, completion: MTRDeviceResponseHandler)](mtrdevice/invokecommand(withendpointid:clusterid:commandid:commandfields:expectedvalues:expectedvalueinterval:timedinvoketimeout:queue:completion:).md)
- [func openCommissioningWindow(withDiscriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t, completion: MTRDeviceOpenCommissioningWindowHandler)](mtrdevice/opencommissioningwindow(withdiscriminator:duration:queue:completion:).md)
- [func openCommissioningWindow(withSetupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t, completion: MTRDeviceOpenCommissioningWindowHandler)](mtrdevice/opencommissioningwindow(withsetuppasscode:discriminator:duration:queue:completion:).md)
- [func readAttribute(withEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, params: MTRReadParams?) -> [String : Any]?](mtrdevice/readattribute(withendpointid:clusterid:attributeid:params:).md)
- [func setDelegate(any MTRDeviceDelegate, queue: dispatch_queue_t)](mtrdevice/setdelegate(_:queue:).md)
- [func writeAttribute(withEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, expectedValueInterval: NSNumber, timedWriteTimeout: NSNumber?)](mtrdevice/writeattribute(withendpointid:clusterid:attributeid:value:expectedvalueinterval:timedwritetimeout:).md)
- [func add(any MTRDeviceDelegate, queue: dispatch_queue_t)](mtrdevice/add(_:queue:).md)
  Adds a delegate to receive asynchronous callbacks about the device.
- [func add(any MTRDeviceDelegate, queue: dispatch_queue_t, interestedPathsForAttributes: [Any]?, interestedPathsForEvents: [Any]?)](mtrdevice/add(_:queue:interestedpathsforattributes:interestedpathsforevents:).md)
  Adds a delegate to receive asynchronous callbacks about the device, and limit attribute and/or event reports to a specific set of paths.
- [func descriptorClusters() -> [MTRAttributePath : [String : Any]]](mtrdevice/descriptorclusters.md)
  Read all known attributes from descriptor clusters on all known endpoints.
- [func invokeCommands([[MTRCommandWithRequiredResponse]], queue: dispatch_queue_t, completion: MTRDeviceResponseHandler)](mtrdevice/invokecommands(_:queue:completion:).md)
  Invoke one or more groups of commands.
- [func readAttributePaths([MTRAttributeRequestPath]) -> [[String : Any]]](mtrdevice/readattributepaths(_:).md)
  Read the attributes identified by the provided attribute paths.  The paths can include wildcards.
- [func remove(any MTRDeviceDelegate)](mtrdevice/remove(_:).md)
  Removes the delegate from receiving callbacks about the device.
- [func wait(forAttributeValues: [MTRAttributePath : [String : Any]], timeout: TimeInterval, queue: dispatch_queue_t, completion: ((any Error)?) -> Void) -> MTRAttributeValueWaiter](mtrdevice/wait(forattributevalues:timeout:queue:completion:).md)
  Sets up the provided completion to be called when any of the following happens:

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice)*