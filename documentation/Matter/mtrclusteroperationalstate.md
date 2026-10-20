# MTRClusterOperationalState

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
class MTRClusterOperationalState
```

```objc
@interface MTRClusterOperationalState : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteroperationalstate/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func pause(with: MTROperationalStateClusterPauseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalstate/pause%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func pause(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalstate/pause%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributeclusterrevision%28with%29.md)
- [func readAttributeCountdownTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributecountdowntime%28with%29.md)
- [func readAttributeCurrentPhase(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributecurrentphase%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOperationalError(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributeoperationalerror%28with%29.md)
- [func readAttributeOperationalState(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributeoperationalstate%28with%29.md)
- [func readAttributeOperationalStateList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributeoperationalstatelist%28with%29.md)
- [func readAttributePhaseList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalstate/readattributephaselist%28with%29.md)
- [func resume(with: MTROperationalStateClusterResumeParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalstate/resume%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resume(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalstate/resume%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func start(with: MTROperationalStateClusterStartParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalstate/start%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func start(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalstate/start%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func stop(with: MTROperationalStateClusterStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalstate/stop%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalstate/stop%28withexpectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteroperationalstate)*