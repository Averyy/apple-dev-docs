# MTRBaseClusterBasic

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use MTRBaseClusterBasicInformation

## Declaration

```swift
class MTRBaseClusterBasic
```

```objc
@interface MTRBaseClusterBasic : MTRBaseClusterBasicInformation
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterbasic/init%28device,endpoint,queue%29.md)
### Instance Methods
- [func mfgSpecificPing(completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbasic/mfgspecificping%28completionhandler%29.md)
- [func mfgSpecificPing(with: MTRBasicClusterMfgSpecificPingParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbasic/mfgspecificping%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeCapabilityMinima(completionHandler: (MTRBasicClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributecapabilityminima%28completionhandler%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeDataModelRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributedatamodelrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeHardwareVersion(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributehardwareversion%28completionhandler%29.md)
- [func readAttributeHardwareVersionString(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributehardwareversionstring%28completionhandler%29.md)
- [func readAttributeLocalConfigDisabled(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributelocalconfigdisabled%28completionhandler%29.md)
- [func readAttributeLocation(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributelocation%28completionhandler%29.md)
- [func readAttributeManufacturingDate(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributemanufacturingdate%28completionhandler%29.md)
- [func readAttributeNodeLabel(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributenodelabel%28completionhandler%29.md)
- [func readAttributePartNumber(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributepartnumber%28completionhandler%29.md)
- [func readAttributeProductID(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeproductid%28completionhandler%29.md)
- [func readAttributeProductLabel(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeproductlabel%28completionhandler%29.md)
- [func readAttributeProductName(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeproductname%28completionhandler%29.md)
- [func readAttributeProductURL(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeproducturl%28completionhandler%29.md)
- [func readAttributeReachable(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributereachable%28completionhandler%29.md)
- [func readAttributeSerialNumber(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeserialnumber%28completionhandler%29.md)
- [func readAttributeSoftwareVersion(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributesoftwareversion%28completionhandler%29.md)
- [func readAttributeSoftwareVersionString(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributesoftwareversionstring%28completionhandler%29.md)
- [func readAttributeUniqueID(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeuniqueid%28completionhandler%29.md)
- [func readAttributeVendorID(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributevendorid%28completionhandler%29.md)
- [func readAttributeVendorName(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributevendorname%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCapabilityMinima(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRBasicClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributecapabilityminima%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDataModelRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributedatamodelrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareVersion(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributehardwareversion%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareVersionString(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributehardwareversionstring%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLocalConfigDisabled(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributelocalconfigdisabled%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLocation(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributelocation%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeManufacturingDate(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributemanufacturingdate%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNodeLabel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributenodelabel%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePartNumber(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributepartnumber%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeproductid%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductLabel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeproductlabel%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductName(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeproductname%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductURL(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeproducturl%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReachable(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributereachable%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSerialNumber(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeserialnumber%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSoftwareVersion(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributesoftwareversion%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSoftwareVersionString(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributesoftwareversionstring%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUniqueID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributeuniqueid%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVendorID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributevendorid%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVendorName(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/subscribeattributevendorname%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeLocalConfigDisabled(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbasic/writeattributelocalconfigdisabled%28withvalue,completionhandler%29.md)
- [func writeAttributeLocalConfigDisabled(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbasic/writeattributelocalconfigdisabled%28withvalue,params,completionhandler%29.md)
- [func writeAttributeLocation(withValue: String, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbasic/writeattributelocation%28withvalue,completionhandler%29.md)
- [func writeAttributeLocation(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbasic/writeattributelocation%28withvalue,params,completionhandler%29.md)
- [func writeAttributeNodeLabel(withValue: String, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbasic/writeattributenodelabel%28withvalue,completionhandler%29.md)
- [func writeAttributeNodeLabel(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbasic/writeattributenodelabel%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCapabilityMinima(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRBasicClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributecapabilityminima%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeDataModelRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributedatamodelrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeHardwareVersion(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributehardwareversion%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeHardwareVersionString(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributehardwareversionstring%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeLocalConfigDisabled(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributelocalconfigdisabled%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeLocation(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributelocation%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeManufacturingDate(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributemanufacturingdate%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeNodeLabel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributenodelabel%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePartNumber(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributepartnumber%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeProductID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeproductid%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeProductLabel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeproductlabel%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeProductName(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeproductname%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeProductURL(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeproducturl%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeReachable(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributereachable%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSerialNumber(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeserialnumber%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSoftwareVersion(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributesoftwareversion%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSoftwareVersionString(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributesoftwareversionstring%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeUniqueID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributeuniqueid%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeVendorID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributevendorid%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeVendorName(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasic/readattributevendorname%28withattributecache,endpoint,queue,completionhandler%29.md)

## Relationships

### Inherits From
- [MTRBaseClusterBasicInformation](./mtrbaseclusterbasicinformation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasic)*