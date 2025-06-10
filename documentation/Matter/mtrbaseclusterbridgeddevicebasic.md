# MTRBaseClusterBridgedDeviceBasic

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
class MTRBaseClusterBridgedDeviceBasic
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterbridgeddevicebasic/init(device:endpoint:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeHardwareVersion(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributehardwareversion(completionhandler:).md)
- [func readAttributeHardwareVersionString(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributehardwareversionstring(completionhandler:).md)
- [func readAttributeManufacturingDate(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributemanufacturingdate(completionhandler:).md)
- [func readAttributeNodeLabel(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributenodelabel(completionhandler:).md)
- [func readAttributePartNumber(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributepartnumber(completionhandler:).md)
- [func readAttributeProductLabel(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeproductlabel(completionhandler:).md)
- [func readAttributeProductName(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeproductname(completionhandler:).md)
- [func readAttributeProductURL(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeproducturl(completionhandler:).md)
- [func readAttributeReachable(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributereachable(completionhandler:).md)
- [func readAttributeSerialNumber(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeserialnumber(completionhandler:).md)
- [func readAttributeSoftwareVersion(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributesoftwareversion(completionhandler:).md)
- [func readAttributeSoftwareVersionString(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributesoftwareversionstring(completionhandler:).md)
- [func readAttributeUniqueID(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeuniqueid(completionhandler:).md)
- [func readAttributeVendorID(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributevendorid(completionhandler:).md)
- [func readAttributeVendorName(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributevendorname(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareVersion(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributehardwareversion(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareVersionString(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributehardwareversionstring(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeManufacturingDate(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributemanufacturingdate(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNodeLabel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributenodelabel(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePartNumber(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributepartnumber(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductLabel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributeproductlabel(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductName(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributeproductname(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductURL(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributeproducturl(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReachable(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributereachable(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSerialNumber(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributeserialnumber(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSoftwareVersion(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributesoftwareversion(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSoftwareVersionString(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributesoftwareversionstring(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUniqueID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributeuniqueid(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVendorID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributevendorid(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVendorName(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/subscribeattributevendorname(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeNodeLabel(withValue: String, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/writeattributenodelabel(withvalue:completionhandler:).md)
- [func writeAttributeNodeLabel(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/writeattributenodelabel(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeHardwareVersion(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributehardwareversion(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeHardwareVersionString(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributehardwareversionstring(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeManufacturingDate(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributemanufacturingdate(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeNodeLabel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributenodelabel(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePartNumber(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributepartnumber(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeProductLabel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeproductlabel(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeProductName(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeproductname(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeProductURL(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeproducturl(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeReachable(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributereachable(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSerialNumber(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeserialnumber(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSoftwareVersion(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributesoftwareversion(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSoftwareVersionString(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributesoftwareversionstring(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeUniqueID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributeuniqueid(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeVendorID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributevendorid(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeVendorName(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasic/readattributevendorname(withattributecache:endpoint:queue:completionhandler:).md)

## Relationships

### Inherits From
- [MTRBaseClusterBridgedDeviceBasicInformation](mtrbaseclusterbridgeddevicebasicinformation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbridgeddevicebasic)*