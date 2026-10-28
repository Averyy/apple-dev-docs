# MTRBaseClusterEnergyEVSE

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Energy EVSE

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRBaseClusterEnergyEVSE
```

```objc
@interface MTRBaseClusterEnergyEVSE : MTRGenericBaseCluster
```

## Overview

Electric Vehicle Supply Equipment (EVSE) is equipment used to charge an Electric Vehicle (EV) or Plug-In Hybrid Electric Vehicle. This cluster provides an interface to the functionality of Electric Vehicle Supply Equipment (EVSE) management.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterenergyevse/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func clearTargets(completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/cleartargets%28completion%29.md)
- [func clearTargets(with: MTREnergyEVSEClusterClearTargetsParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/cleartargets%28with,completion%29.md)
  Command ClearTargets
- [func disable(completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/disable%28completion%29.md)
- [func disable(with: MTREnergyEVSEClusterDisableParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/disable%28with,completion%29.md)
  Command Disable
- [func enableCharging(with: MTREnergyEVSEClusterEnableChargingParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/enablecharging%28with,completion%29.md)
  Command EnableCharging
- [func getTargetsWith(MTREnergyEVSEClusterGetTargetsParams?, completion: (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/gettargetswith%28_,completion%29.md)
  Command GetTargets
- [func getTargetsWithCompletion((MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/gettargetswithcompletion%28_%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeApproximateEVEfficiency(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeapproximateevefficiency%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeattributelist%28completion%29.md)
- [func readAttributeChargingEnabledUntil(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributechargingenableduntil%28completion%29.md)
- [func readAttributeCircuitCapacity(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributecircuitcapacity%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFaultState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributefaultstate%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeMaximumChargeCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributemaximumchargecurrent%28completion%29.md)
- [func readAttributeMinimumChargeCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeminimumchargecurrent%28completion%29.md)
- [func readAttributeNextChargeRequiredEnergy(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributenextchargerequiredenergy%28completion%29.md)
- [func readAttributeNextChargeStartTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributenextchargestarttime%28completion%29.md)
- [func readAttributeNextChargeTargetSoC(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributenextchargetargetsoc%28completion%29.md)
- [func readAttributeNextChargeTargetTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributenextchargetargettime%28completion%29.md)
- [func readAttributeRandomizationDelayWindow(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributerandomizationdelaywindow%28completion%29.md)
- [func readAttributeSessionDuration(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributesessionduration%28completion%29.md)
- [func readAttributeSessionEnergyCharged(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributesessionenergycharged%28completion%29.md)
- [func readAttributeSessionID(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributesessionid%28completion%29.md)
- [func readAttributeState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributestate%28completion%29.md)
- [func readAttributeSupplyState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributesupplystate%28completion%29.md)
- [func readAttributeUserMaximumChargeCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeusermaximumchargecurrent%28completion%29.md)
- [func setTargetsWith(MTREnergyEVSEClusterSetTargetsParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/settargetswith%28_,completion%29.md)
  Command SetTargets
- [func startDiagnostics(completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/startdiagnostics%28completion%29.md)
- [func startDiagnostics(with: MTREnergyEVSEClusterStartDiagnosticsParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/startdiagnostics%28with,completion%29.md)
  Command StartDiagnostics
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeApproximateEVEfficiency(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributeapproximateevefficiency%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeChargingEnabledUntil(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributechargingenableduntil%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCircuitCapacity(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributecircuitcapacity%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFaultState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributefaultstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaximumChargeCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributemaximumchargecurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMinimumChargeCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributeminimumchargecurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNextChargeRequiredEnergy(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributenextchargerequiredenergy%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNextChargeStartTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributenextchargestarttime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNextChargeTargetSoC(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributenextchargetargetsoc%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNextChargeTargetTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributenextchargetargettime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRandomizationDelayWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributerandomizationdelaywindow%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSessionDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributesessionduration%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSessionEnergyCharged(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributesessionenergycharged%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSessionID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributesessionid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributestate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupplyState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributesupplystate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUserMaximumChargeCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/subscribeattributeusermaximumchargecurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeApproximateEVEfficiency(withValue: NSNumber?, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/writeattributeapproximateevefficiency%28withvalue,completion%29.md)
- [func writeAttributeApproximateEVEfficiency(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/writeattributeapproximateevefficiency%28withvalue,params,completion%29.md)
- [func writeAttributeRandomizationDelayWindow(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/writeattributerandomizationdelaywindow%28withvalue,completion%29.md)
- [func writeAttributeRandomizationDelayWindow(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/writeattributerandomizationdelaywindow%28withvalue,params,completion%29.md)
- [func writeAttributeUserMaximumChargeCurrent(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/writeattributeusermaximumchargecurrent%28withvalue,completion%29.md)
- [func writeAttributeUserMaximumChargeCurrent(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterenergyevse/writeattributeusermaximumchargecurrent%28withvalue,params,completion%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeApproximateEVEfficiency(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeapproximateevefficiency%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeChargingEnabledUntil(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributechargingenableduntil%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCircuitCapacity(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributecircuitcapacity%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFaultState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributefaultstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaximumChargeCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributemaximumchargecurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMinimumChargeCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeminimumchargecurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNextChargeRequiredEnergy(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributenextchargerequiredenergy%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNextChargeStartTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributenextchargestarttime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNextChargeTargetSoC(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributenextchargetargetsoc%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNextChargeTargetTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributenextchargetargettime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRandomizationDelayWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributerandomizationdelaywindow%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSessionDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributesessionduration%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSessionEnergyCharged(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributesessionenergycharged%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSessionID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributesessionid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributestate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupplyState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributesupplystate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUserMaximumChargeCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterenergyevse/readattributeusermaximumchargecurrent%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse)*