# MTRClusterRVCOperationalState

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterRVCOperationalState : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterrvcoperationalstate/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func pause(with: MTRRVCOperationalStateClusterPauseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterrvcoperationalstate/pause%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func pause(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterrvcoperationalstate/pause%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributeclusterrevision%28with%29.md)
- [func readAttributeCountdownTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributecountdowntime%28with%29.md)
- [func readAttributeCurrentPhase(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributecurrentphase%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOperationalError(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributeoperationalerror%28with%29.md)
- [func readAttributeOperationalState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributeoperationalstate%28with%29.md)
- [func readAttributeOperationalStateList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributeoperationalstatelist%28with%29.md)
- [func readAttributePhaseList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvcoperationalstate/readattributephaselist%28with%29.md)
- [func resume(with: MTRRVCOperationalStateClusterResumeParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterrvcoperationalstate/resume%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resume(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterrvcoperationalstate/resume%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func goHome(with: MTRRVCOperationalStateClusterGoHomeParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterrvcoperationalstate/gohome%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func goHome(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterrvcoperationalstate/gohome%28withexpectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterrvcoperationalstate)*