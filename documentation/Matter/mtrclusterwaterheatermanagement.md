# MTRClusterWaterHeaterManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Water Heater Management This cluster is used to allow clients to control the operation of a hot water heating appliance so that it can be used with energy management.

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
class MTRClusterWaterHeaterManagement
```

```objc
@interface MTRClusterWaterHeaterManagement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterwaterheatermanagement/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func boost(with: MTRWaterHeaterManagementClusterBoostParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwaterheatermanagement/boost%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func cancelBoost(with: MTRWaterHeaterManagementClusterCancelBoostParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwaterheatermanagement/cancelboost%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func cancelBoost(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwaterheatermanagement/cancelboost%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributeattributelist%28with%29.md)
- [func readAttributeBoostState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributebooststate%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributeclusterrevision%28with%29.md)
- [func readAttributeEstimatedHeatRequired(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributeestimatedheatrequired%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeHeatDemand(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributeheatdemand%28with%29.md)
- [func readAttributeHeaterTypes(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributeheatertypes%28with%29.md)
- [func readAttributeTankPercentage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributetankpercentage%28with%29.md)
- [func readAttributeTankVolume(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwaterheatermanagement/readattributetankvolume%28with%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterwaterheatermanagement)*