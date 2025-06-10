# MTRClusterWaterHeaterManagement

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterwaterheatermanagement/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func boost(with: MTRWaterHeaterManagementClusterBoostParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwaterheatermanagement/boost(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func cancelBoost(with: MTRWaterHeaterManagementClusterCancelBoostParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwaterheatermanagement/cancelboost(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func cancelBoost(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwaterheatermanagement/cancelboost(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributeattributelist(with:).md)
- [func readAttributeBoostState(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributebooststate(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributeclusterrevision(with:).md)
- [func readAttributeEstimatedHeatRequired(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributeestimatedheatrequired(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributegeneratedcommandlist(with:).md)
- [func readAttributeHeatDemand(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributeheatdemand(with:).md)
- [func readAttributeHeaterTypes(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributeheatertypes(with:).md)
- [func readAttributeTankPercentage(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributetankpercentage(with:).md)
- [func readAttributeTankVolume(with: MTRReadParams?) -> [String : Any]?](mtrclusterwaterheatermanagement/readattributetankvolume(with:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterwaterheatermanagement)*