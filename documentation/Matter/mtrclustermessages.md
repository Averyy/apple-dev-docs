# MTRClusterMessages

**Framework**: Matter  
**Kind**: class

Cluster Messages This cluster provides an interface for passing messages to be presented by a device.

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
class MTRClusterMessages
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustermessages/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func cancelRequest(with: MTRMessagesClusterCancelMessagesRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustermessages/cancelrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func presentRequest(with: MTRMessagesClusterPresentMessagesRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustermessages/presentrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermessages/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveMessageIDs(with: MTRReadParams?) -> [String : Any]?](mtrclustermessages/readattributeactivemessageids(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustermessages/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustermessages/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustermessages/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermessages/readattributegeneratedcommandlist(with:).md)
- [func readAttributeMessages(with: MTRReadParams?) -> [String : Any]?](mtrclustermessages/readattributemessages(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermessages)*