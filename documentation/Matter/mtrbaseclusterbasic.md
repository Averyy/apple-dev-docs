# MTRBaseClusterBasic

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
class MTRBaseClusterBasic
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterbasic/init(device:endpoint:queue:).md)
### Instance Methods
- [func mfgSpecificPing(completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbasic/mfgspecificping(completionhandler:).md)
- [func mfgSpecificPing(with: MTRBasicClusterMfgSpecificPingParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbasic/mfgspecificping(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeattributelist(completionhandler:).md)
- [func readAttributeCapabilityMinima(completionHandler: (MTRBasicClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributecapabilityminima(completionhandler:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeDataModelRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributedatamodelrevision(completionhandler:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeHardwareVersion(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributehardwareversion(completionhandler:).md)
- [func readAttributeHardwareVersionString(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributehardwareversionstring(completionhandler:).md)
- [func readAttributeLocalConfigDisabled(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributelocalconfigdisabled(completionhandler:).md)
- [func readAttributeLocation(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributelocation(completionhandler:).md)
- [func readAttributeManufacturingDate(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributemanufacturingdate(completionhandler:).md)
- [func readAttributeNodeLabel(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributenodelabel(completionhandler:).md)
- [func readAttributePartNumber(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributepartnumber(completionhandler:).md)
- [func readAttributeProductID(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeproductid(completionhandler:).md)
- [func readAttributeProductLabel(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeproductlabel(completionhandler:).md)
- [func readAttributeProductName(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeproductname(completionhandler:).md)
- [func readAttributeProductURL(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeproducturl(completionhandler:).md)
- [func readAttributeReachable(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributereachable(completionhandler:).md)
- [func readAttributeSerialNumber(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeserialnumber(completionhandler:).md)
- [func readAttributeSoftwareVersion(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributesoftwareversion(completionhandler:).md)
- [func readAttributeSoftwareVersionString(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributesoftwareversionstring(completionhandler:).md)
- [func readAttributeUniqueID(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeuniqueid(completionhandler:).md)
- [func readAttributeVendorID(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributevendorid(completionhandler:).md)
- [func readAttributeVendorName(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributevendorname(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCapabilityMinima(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRBasicClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributecapabilityminima(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDataModelRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributedatamodelrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareVersion(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributehardwareversion(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareVersionString(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributehardwareversionstring(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLocalConfigDisabled(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributelocalconfigdisabled(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLocation(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributelocation(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeManufacturingDate(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributemanufacturingdate(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNodeLabel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributenodelabel(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePartNumber(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributepartnumber(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeproductid(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductLabel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeproductlabel(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductName(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeproductname(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductURL(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeproducturl(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReachable(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributereachable(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSerialNumber(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeserialnumber(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSoftwareVersion(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributesoftwareversion(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSoftwareVersionString(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributesoftwareversionstring(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUniqueID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributeuniqueid(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVendorID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributevendorid(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVendorName(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/subscribeattributevendorname(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeLocalConfigDisabled(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbasic/writeattributelocalconfigdisabled(withvalue:completionhandler:).md)
- [func writeAttributeLocalConfigDisabled(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbasic/writeattributelocalconfigdisabled(withvalue:params:completionhandler:).md)
- [func writeAttributeLocation(withValue: String, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbasic/writeattributelocation(withvalue:completionhandler:).md)
- [func writeAttributeLocation(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbasic/writeattributelocation(withvalue:params:completionhandler:).md)
- [func writeAttributeNodeLabel(withValue: String, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbasic/writeattributenodelabel(withvalue:completionhandler:).md)
- [func writeAttributeNodeLabel(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbasic/writeattributenodelabel(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCapabilityMinima(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRBasicClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributecapabilityminima(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeDataModelRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributedatamodelrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeHardwareVersion(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributehardwareversion(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeHardwareVersionString(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributehardwareversionstring(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeLocalConfigDisabled(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributelocalconfigdisabled(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeLocation(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributelocation(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeManufacturingDate(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributemanufacturingdate(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeNodeLabel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributenodelabel(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePartNumber(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributepartnumber(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeProductID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeproductid(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeProductLabel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeproductlabel(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeProductName(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeproductname(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeProductURL(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeproducturl(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeReachable(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributereachable(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSerialNumber(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeserialnumber(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSoftwareVersion(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributesoftwareversion(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSoftwareVersionString(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributesoftwareversionstring(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeUniqueID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributeuniqueid(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeVendorID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributevendorid(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeVendorName(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasic/readattributevendorname(withattributecache:endpoint:queue:completionhandler:).md)

## Relationships

### Inherits From
- [MTRBaseClusterBasicInformation](mtrbaseclusterbasicinformation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasic)*