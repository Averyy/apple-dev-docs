# MTRClusterRVCOperationalState

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
class MTRClusterRVCOperationalState
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterrvcoperationalstate/init(device:endpointid:queue:).md)
### Instance Methods
- [func pause(with: MTRRVCOperationalStateClusterPauseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterrvcoperationalstate/pause(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func pause(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterrvcoperationalstate/pause(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributeclusterrevision(with:).md)
- [func readAttributeCountdownTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributecountdowntime(with:).md)
- [func readAttributeCurrentPhase(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributecurrentphase(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOperationalError(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributeoperationalerror(with:).md)
- [func readAttributeOperationalState(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributeoperationalstate(with:).md)
- [func readAttributeOperationalStateList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributeoperationalstatelist(with:).md)
- [func readAttributePhaseList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvcoperationalstate/readattributephaselist(with:).md)
- [func resume(with: MTRRVCOperationalStateClusterResumeParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterrvcoperationalstate/resume(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resume(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterrvcoperationalstate/resume(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func goHome(with: MTRRVCOperationalStateClusterGoHomeParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterrvcoperationalstate/gohome(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func goHome(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrclusterrvcoperationalstate/gohome(withexpectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterrvcoperationalstate)*