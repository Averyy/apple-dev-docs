# MTRClusterOvenCavityOperationalState

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterOvenCavityOperationalState : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterovencavityoperationalstate/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributeclusterrevision%28with%29.md)
- [func readAttributeCountdownTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributecountdowntime%28with%29.md)
- [func readAttributeCurrentPhase(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributecurrentphase%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOperationalError(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributeoperationalerror%28with%29.md)
- [func readAttributeOperationalState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributeoperationalstate%28with%29.md)
- [func readAttributeOperationalStateList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributeoperationalstatelist%28with%29.md)
- [func readAttributePhaseList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterovencavityoperationalstate/readattributephaselist%28with%29.md)
- [func start(with: MTROvenCavityOperationalStateClusterStartParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterovencavityoperationalstate/start%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func start(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterovencavityoperationalstate/start%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func stop(with: MTROvenCavityOperationalStateClusterStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterovencavityoperationalstate/stop%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrclusterovencavityoperationalstate/stop%28withexpectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterovencavityoperationalstate)*