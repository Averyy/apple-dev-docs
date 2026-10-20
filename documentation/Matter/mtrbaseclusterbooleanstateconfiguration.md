# MTRBaseClusterBooleanStateConfiguration

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRBaseClusterBooleanStateConfiguration
```

```objc
@interface MTRBaseClusterBooleanStateConfiguration : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterbooleanstateconfiguration/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func enableDisableAlarm(with: MTRBooleanStateConfigurationClusterEnableDisableAlarmParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/enabledisablealarm%28with,completion%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAlarmsActive(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributealarmsactive%28completion%29.md)
- [func readAttributeAlarmsEnabled(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributealarmsenabled%28completion%29.md)
- [func readAttributeAlarmsSupported(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributealarmssupported%28completion%29.md)
- [func readAttributeAlarmsSuppressed(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributealarmssuppressed%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCurrentSensitivityLevel(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributecurrentsensitivitylevel%28completion%29.md)
- [func readAttributeDefaultSensitivityLevel(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributedefaultsensitivitylevel%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeSensorFault(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributesensorfault%28completion%29.md)
- [func readAttributeSupportedSensitivityLevels(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributesupportedsensitivitylevels%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAlarmsActive(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributealarmsactive%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAlarmsEnabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributealarmsenabled%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAlarmsSupported(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributealarmssupported%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAlarmsSuppressed(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributealarmssuppressed%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentSensitivityLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributecurrentsensitivitylevel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDefaultSensitivityLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributedefaultsensitivitylevel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSensorFault(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributesensorfault%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedSensitivityLevels(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/subscribeattributesupportedsensitivitylevels%28with,subscriptionestablished,reporthandler%29.md)
- [func suppressAlarm(with: MTRBooleanStateConfigurationClusterSuppressAlarmParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/suppressalarm%28with,completion%29.md)
- [func writeAttributeCurrentSensitivityLevel(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/writeattributecurrentsensitivitylevel%28withvalue,completion%29.md)
- [func writeAttributeCurrentSensitivityLevel(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/writeattributecurrentsensitivitylevel%28withvalue,params,completion%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAlarmsActive(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributealarmsactive%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAlarmsEnabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributealarmsenabled%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAlarmsSupported(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributealarmssupported%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAlarmsSuppressed(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributealarmssuppressed%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentSensitivityLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributecurrentsensitivitylevel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDefaultSensitivityLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributedefaultsensitivitylevel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSensorFault(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributesensorfault%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedSensitivityLevels(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbooleanstateconfiguration/readattributesupportedsensitivitylevels%28withclusterstatecache,endpoint,queue,completion%29.md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](./mtrgenericbasecluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbooleanstateconfiguration)*