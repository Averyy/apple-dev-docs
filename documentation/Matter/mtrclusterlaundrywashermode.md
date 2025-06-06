# MTRClusterLaundryWasherMode

**Framework**: Matter  
**Kind**: class

Cluster Laundry Washer Mode Attributes and commands for selecting a mode from a list of supported options.

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
class MTRClusterLaundryWasherMode
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterlaundrywashermode/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func changeToMode(with: MTRLaundryWasherModeClusterChangeToModeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRLaundryWasherModeClusterChangeToModeResponseParams?, (any Error)?) -> Void)](mtrclusterlaundrywashermode/changetomode(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashermode/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashermode/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashermode/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashermode/readattributecurrentmode(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashermode/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashermode/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSupportedModes(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashermode/readattributesupportedmodes(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterlaundrywashermode)*