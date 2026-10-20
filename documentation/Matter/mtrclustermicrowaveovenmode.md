# MTRClusterMicrowaveOvenMode

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Microwave Oven Mode Attributes and commands for selecting a mode from a list of supported options.

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
class MTRClusterMicrowaveOvenMode
```

```objc
@interface MTRClusterMicrowaveOvenMode : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustermicrowaveovenmode/init%28device,endpointid,queue%29.md)
  The queue is currently unused, but may be used in the future for calling completions for command invocations if commands are added to this cluster.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovenmode/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovenmode/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovenmode/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentMode(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovenmode/readattributecurrentmode%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovenmode/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovenmode/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSupportedModes(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovenmode/readattributesupportedmodes%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermicrowaveovenmode)*