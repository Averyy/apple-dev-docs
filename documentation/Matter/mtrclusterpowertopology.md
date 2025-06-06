# MTRClusterPowerTopology

**Framework**: Matter  
**Kind**: class

Cluster Power Topology The Power Topology Cluster provides a mechanism for expressing how power is flowing between endpoints.

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
class MTRClusterPowerTopology
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterpowertopology/init(device:endpointid:queue:).md)
  The queue is currently unused, but may be used in the future for calling completions for command invocations if commands are added to this cluster.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowertopology/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveEndpoints(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowertopology/readattributeactiveendpoints(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowertopology/readattributeattributelist(with:).md)
- [func readAttributeAvailableEndpoints(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowertopology/readattributeavailableendpoints(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowertopology/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowertopology/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowertopology/readattributegeneratedcommandlist(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterpowertopology)*