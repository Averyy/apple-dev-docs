# MTRBaseClusterDeviceEnergyManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Device Energy Management

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
class MTRBaseClusterDeviceEnergyManagement
```

```objc
@interface MTRBaseClusterDeviceEnergyManagement : MTRGenericBaseCluster
```

#### Overview

This cluster allows a client to manage the power draw of a device. An example of such a client could be an Energy Management System (EMS) which controls an Energy Smart Appliance (ESA).

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterdeviceenergymanagement/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func cancelPowerAdjustRequest(completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/cancelpoweradjustrequest%28completion%29.md)
- [func cancelPowerAdjustRequest(with: MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/cancelpoweradjustrequest%28with,completion%29.md)
  Command CancelPowerAdjustRequest
- [func cancelRequest(completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/cancelrequest%28completion%29.md)
- [func cancelRequest(with: MTRDeviceEnergyManagementClusterCancelRequestParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/cancelrequest%28with,completion%29.md)
  Command CancelRequest
- [func modifyForecastRequest(with: MTRDeviceEnergyManagementClusterModifyForecastRequestParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/modifyforecastrequest%28with,completion%29.md)
  Command ModifyForecastRequest
- [func pauseRequest(with: MTRDeviceEnergyManagementClusterPauseRequestParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/pauserequest%28with,completion%29.md)
  Command PauseRequest
- [func powerAdjustRequest(with: MTRDeviceEnergyManagementClusterPowerAdjustRequestParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/poweradjustrequest%28with,completion%29.md)
  Command PowerAdjustRequest
- [func readAttributeAbsMaxPower(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeabsmaxpower%28completion%29.md)
- [func readAttributeAbsMinPower(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeabsminpower%28completion%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeESACanGenerate(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeesacangenerate%28completion%29.md)
- [func readAttributeESAState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeesastate%28completion%29.md)
- [func readAttributeESAType(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeesatype%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributefeaturemap%28completion%29.md)
- [func readAttributeForecast(completion: (MTRDeviceEnergyManagementClusterForecastStruct?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeforecast%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeOptOutState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeoptoutstate%28completion%29.md)
- [func readAttributePowerAdjustmentCapability(completion: (MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributepoweradjustmentcapability%28completion%29.md)
- [func requestConstraintBasedForecast(with: MTRDeviceEnergyManagementClusterRequestConstraintBasedForecastParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/requestconstraintbasedforecast%28with,completion%29.md)
  Command RequestConstraintBasedForecast
- [func resumeRequest(completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/resumerequest%28completion%29.md)
- [func resumeRequest(with: MTRDeviceEnergyManagementClusterResumeRequestParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/resumerequest%28with,completion%29.md)
  Command ResumeRequest
- [func startTimeAdjustRequest(with: MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/starttimeadjustrequest%28with,completion%29.md)
  Command StartTimeAdjustRequest
- [func subscribeAttributeAbsMaxPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeabsmaxpower%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAbsMinPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeabsminpower%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeESACanGenerate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeesacangenerate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeESAState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeesastate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeESAType(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeesatype%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeForecast(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRDeviceEnergyManagementClusterForecastStruct?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeforecast%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOptOutState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributeoptoutstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePowerAdjustmentCapability(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/subscribeattributepoweradjustmentcapability%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAbsMaxPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeabsmaxpower%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAbsMinPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeabsminpower%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeESACanGenerate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeesacangenerate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeESAState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeesastate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeESAType(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeesatype%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeForecast(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRDeviceEnergyManagementClusterForecastStruct?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeforecast%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOptOutState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributeoptoutstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePowerAdjustmentCapability(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct?, (any Error)?) -> Void)](./mtrbaseclusterdeviceenergymanagement/readattributepoweradjustmentcapability%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement)*