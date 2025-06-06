# MTRClusterOvenCavityOperationalState

**Framework**: Matter  
**Kind**: class

Cluster Oven Cavity Operational State This cluster supports remotely monitoring and, where supported, changing the operational state of an Oven.

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
class MTRClusterOvenCavityOperationalState
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterovencavityoperationalstate/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributeclusterrevision(with:).md)
- [func readAttributeCountdownTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributecountdowntime(with:).md)
- [func readAttributeCurrentPhase(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributecurrentphase(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOperationalError(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributeoperationalerror(with:).md)
- [func readAttributeOperationalState(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributeoperationalstate(with:).md)
- [func readAttributeOperationalStateList(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributeoperationalstatelist(with:).md)
- [func readAttributePhaseList(with: MTRReadParams?) -> [String : Any]?](mtrclusterovencavityoperationalstate/readattributephaselist(with:).md)
- [func start(with: MTROvenCavityOperationalStateClusterStartParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterovencavityoperationalstate/start(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func start(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterovencavityoperationalstate/start(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func stop(with: MTROvenCavityOperationalStateClusterStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterovencavityoperationalstate/stop(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterovencavityoperationalstate/stop(withexpectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterovencavityoperationalstate)*