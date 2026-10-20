# MTRBaseClusterBridgedDeviceBasic

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 17.0
- iPadOS 16.1+ - Deprecated in 17.0
- Mac Catalyst 16.1+ - Deprecated in 17.0
- macOS 13.0+ - Deprecated in 14.0
- tvOS 16.1+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 10.0

> **Deprecated**: Please use MTRBaseClusterBridgedDeviceBasicInformation

## Declaration

```swift
class MTRBaseClusterBridgedDeviceBasic
```

```objc
@interface MTRBaseClusterBridgedDeviceBasic : MTRBaseClusterBridgedDeviceBasicInformation
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterbridgeddevicebasic/init%28device,endpoint,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeHardwareVersion(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributehardwareversion%28completionhandler%29.md)
- [func readAttributeHardwareVersionString(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributehardwareversionstring%28completionhandler%29.md)
- [func readAttributeManufacturingDate(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributemanufacturingdate%28completionhandler%29.md)
- [func readAttributeNodeLabel(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributenodelabel%28completionhandler%29.md)
- [func readAttributePartNumber(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributepartnumber%28completionhandler%29.md)
- [func readAttributeProductLabel(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeproductlabel%28completionhandler%29.md)
- [func readAttributeProductName(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeproductname%28completionhandler%29.md)
- [func readAttributeProductURL(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeproducturl%28completionhandler%29.md)
- [func readAttributeReachable(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributereachable%28completionhandler%29.md)
- [func readAttributeSerialNumber(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeserialnumber%28completionhandler%29.md)
- [func readAttributeSoftwareVersion(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributesoftwareversion%28completionhandler%29.md)
- [func readAttributeSoftwareVersionString(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributesoftwareversionstring%28completionhandler%29.md)
- [func readAttributeUniqueID(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeuniqueid%28completionhandler%29.md)
- [func readAttributeVendorID(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributevendorid%28completionhandler%29.md)
- [func readAttributeVendorName(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributevendorname%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareVersion(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributehardwareversion%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareVersionString(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributehardwareversionstring%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeManufacturingDate(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributemanufacturingdate%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNodeLabel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributenodelabel%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePartNumber(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributepartnumber%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductLabel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributeproductlabel%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductName(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributeproductname%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductURL(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributeproducturl%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReachable(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributereachable%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSerialNumber(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributeserialnumber%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSoftwareVersion(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributesoftwareversion%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSoftwareVersionString(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributesoftwareversionstring%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUniqueID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributeuniqueid%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVendorID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributevendorid%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVendorName(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/subscribeattributevendorname%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeNodeLabel(withValue: String, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/writeattributenodelabel%28withvalue,completionhandler%29.md)
- [func writeAttributeNodeLabel(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/writeattributenodelabel%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeHardwareVersion(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributehardwareversion%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeHardwareVersionString(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributehardwareversionstring%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeManufacturingDate(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributemanufacturingdate%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeNodeLabel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributenodelabel%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePartNumber(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributepartnumber%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeProductLabel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeproductlabel%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeProductName(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeproductname%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeProductURL(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeproducturl%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeReachable(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributereachable%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSerialNumber(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeserialnumber%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSoftwareVersion(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributesoftwareversion%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSoftwareVersionString(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributesoftwareversionstring%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeUniqueID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributeuniqueid%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeVendorID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributevendorid%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeVendorName(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasic/readattributevendorname%28withattributecache,endpoint,queue,completionhandler%29.md)

## Relationships

### Inherits From
- [MTRBaseClusterBridgedDeviceBasicInformation](./mtrbaseclusterbridgeddevicebasicinformation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbridgeddevicebasic)*