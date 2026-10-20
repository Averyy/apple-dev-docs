# MTRClusterPowerTopology

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterPowerTopology : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterpowertopology/init%28device,endpointid,queue%29.md)
  The queue is currently unused, but may be used in the future for calling completions for command invocations if commands are added to this cluster.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowertopology/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveEndpoints(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowertopology/readattributeactiveendpoints%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowertopology/readattributeattributelist%28with%29.md)
- [func readAttributeAvailableEndpoints(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowertopology/readattributeavailableendpoints%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowertopology/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowertopology/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowertopology/readattributegeneratedcommandlist%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterpowertopology)*