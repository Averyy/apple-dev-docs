# MTRBaseDevice

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
class MTRBaseDevice
```

## Topics

### Initializers
- [init(nodeID: NSNumber, controller: MTRDeviceController)](mtrbasedevice/init(nodeid:controller:).md)
### Instance Properties
- [var sessionTransportType: MTRTransportType](mtrbasedevice/sessiontransporttype.md)
### Instance Methods
- [func deregisterReportHandlers(with: dispatch_queue_t, completion: () -> Void)](mtrbasedevice/deregisterreporthandlers(with:completion:).md)
- [func deregisterReportHandlers(withClientQueue: dispatch_queue_t, completion: () -> Void)](mtrbasedevice/deregisterreporthandlers(withclientqueue:completion:).md)
- [func downloadLog(of: MTRDiagnosticLogType, timeout: TimeInterval, queue: dispatch_queue_t, completion: (URL?, (any Error)?) -> Void)](mtrbasedevice/downloadlog(of:timeout:queue:completion:).md)
- [func invokeCommand(withEndpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, timedInvokeTimeout: NSNumber?, queue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](mtrbasedevice/invokecommand(withendpointid:clusterid:commandid:commandfields:timedinvoketimeout:queue:completion:).md)
- [func invokeCommand(withEndpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber, commandFields: Any, timedInvokeTimeout: NSNumber?, clientQueue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](mtrbasedevice/invokecommand(withendpointid:clusterid:commandid:commandfields:timedinvoketimeout:clientqueue:completion:).md)
- [func openCommissioningWindow(withDiscriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t, completion: (MTRSetupPayload?, (any Error)?) -> Void)](mtrbasedevice/opencommissioningwindow(withdiscriminator:duration:queue:completion:).md)
- [func openCommissioningWindow(withSetupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t, completion: (MTRSetupPayload?, (any Error)?) -> Void)](mtrbasedevice/opencommissioningwindow(withsetuppasscode:discriminator:duration:queue:completion:).md)
- [func readAttribute(withEndpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, params: MTRReadParams?, clientQueue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](mtrbasedevice/readattribute(withendpointid:clusterid:attributeid:params:clientqueue:completion:).md)
- [func readAttributePaths([MTRAttributeRequestPath]?, eventPaths: [MTREventRequestPath]?, params: MTRReadParams?, queue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](mtrbasedevice/readattributepaths(_:eventpaths:params:queue:completion:).md)
- [func readAttributes(withEndpointID: NSNumber?, clusterID: NSNumber?, attributeID: NSNumber?, params: MTRReadParams?, queue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](mtrbasedevice/readattributes(withendpointid:clusterid:attributeid:params:queue:completion:).md)
- [func readEvents(withEndpointID: NSNumber?, clusterID: NSNumber?, eventID: NSNumber?, params: MTRReadParams?, queue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](mtrbasedevice/readevents(withendpointid:clusterid:eventid:params:queue:completion:).md)
- [func subscribe(toAttributePaths: [MTRAttributeRequestPath]?, eventPaths: [MTREventRequestPath]?, params: MTRSubscribeParams?, queue: dispatch_queue_t, reportHandler: MTRDeviceResponseHandler, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, resubscriptionScheduled: MTRDeviceResubscriptionScheduledHandler?)](mtrbasedevice/subscribe(toattributepaths:eventpaths:params:queue:reporthandler:subscriptionestablished:resubscriptionscheduled:).md)
- [func subscribe(with: dispatch_queue_t, minInterval: UInt16, maxInterval: UInt16, params: MTRSubscribeParams?, cacheContainer: MTRAttributeCacheContainer?, attributeReportHandler: MTRDeviceReportHandler?, eventReportHandler: MTRDeviceReportHandler?, errorHandler: MTRDeviceErrorHandler, subscriptionEstablished: (() -> Void)?, resubscriptionScheduled: MTRDeviceResubscriptionScheduledHandler?)](mtrbasedevice/subscribe(with:mininterval:maxinterval:params:cachecontainer:attributereporthandler:eventreporthandler:errorhandler:subscriptionestablished:resubscriptionscheduled:).md)
- [func subscribe(with: dispatch_queue_t, params: MTRSubscribeParams, clusterStateCacheContainer: MTRClusterStateCacheContainer?, attributeReportHandler: MTRDeviceReportHandler?, eventReportHandler: MTRDeviceReportHandler?, errorHandler: MTRDeviceErrorHandler, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, resubscriptionScheduled: MTRDeviceResubscriptionScheduledHandler?)](mtrbasedevice/subscribe(with:params:clusterstatecachecontainer:attributereporthandler:eventreporthandler:errorhandler:subscriptionestablished:resubscriptionscheduled:).md)
- [func subscribeAttribute(withEndpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, minInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, clientQueue: dispatch_queue_t, reportHandler: MTRDeviceResponseHandler, subscriptionEstablished: (() -> Void)?)](mtrbasedevice/subscribeattribute(withendpointid:clusterid:attributeid:mininterval:maxinterval:params:clientqueue:reporthandler:subscriptionestablished:).md)
- [func subscribeToAttributes(withEndpointID: NSNumber?, clusterID: NSNumber?, attributeID: NSNumber?, params: MTRSubscribeParams?, queue: dispatch_queue_t, reportHandler: MTRDeviceResponseHandler, subscriptionEstablished: MTRSubscriptionEstablishedHandler?)](mtrbasedevice/subscribetoattributes(withendpointid:clusterid:attributeid:params:queue:reporthandler:subscriptionestablished:).md)
- [func subscribeToEvents(withEndpointID: NSNumber?, clusterID: NSNumber?, eventID: NSNumber?, params: MTRSubscribeParams?, queue: dispatch_queue_t, reportHandler: MTRDeviceResponseHandler, subscriptionEstablished: MTRSubscriptionEstablishedHandler?)](mtrbasedevice/subscribetoevents(withendpointid:clusterid:eventid:params:queue:reporthandler:subscriptionestablished:).md)
- [func writeAttribute(withEndpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, timedWriteTimeout: NSNumber?, queue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](mtrbasedevice/writeattribute(withendpointid:clusterid:attributeid:value:timedwritetimeout:queue:completion:).md)
- [func writeAttribute(withEndpointId: NSNumber, clusterId: NSNumber, attributeId: NSNumber, value: Any, timedWriteTimeout: NSNumber?, clientQueue: dispatch_queue_t, completion: ([[String : Any]]?, (any Error)?) -> Void)](mtrbasedevice/writeattribute(withendpointid:clusterid:attributeid:value:timedwritetimeout:clientqueue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice)*