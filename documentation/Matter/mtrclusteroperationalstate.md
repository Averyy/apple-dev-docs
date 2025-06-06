# MTRClusterOperationalState

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
class MTRClusterOperationalState
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteroperationalstate/init(device:endpointid:queue:).md)
### Instance Methods
- [func pause(with: MTROperationalStateClusterPauseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalstate/pause(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func pause(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalstate/pause(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributeclusterrevision(with:).md)
- [func readAttributeCountdownTime(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributecountdowntime(with:).md)
- [func readAttributeCurrentPhase(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributecurrentphase(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOperationalError(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributeoperationalerror(with:).md)
- [func readAttributeOperationalState(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributeoperationalstate(with:).md)
- [func readAttributeOperationalStateList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributeoperationalstatelist(with:).md)
- [func readAttributePhaseList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalstate/readattributephaselist(with:).md)
- [func resume(with: MTROperationalStateClusterResumeParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalstate/resume(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resume(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalstate/resume(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func start(with: MTROperationalStateClusterStartParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalstate/start(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func start(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalstate/start(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func stop(with: MTROperationalStateClusterStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalstate/stop(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalstate/stop(withexpectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteroperationalstate)*