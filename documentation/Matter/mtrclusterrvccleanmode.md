# MTRClusterRVCCleanMode

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
class MTRClusterRVCCleanMode
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterrvccleanmode/init(device:endpointid:queue:).md)
### Instance Methods
- [func changeToMode(with: MTRRVCCleanModeClusterChangeToModeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCCleanModeClusterChangeToModeResponseParams?, (any Error)?) -> Void)](mtrclusterrvccleanmode/changetomode(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvccleanmode/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvccleanmode/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvccleanmode/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvccleanmode/readattributecurrentmode(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvccleanmode/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvccleanmode/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSupportedModes(with: MTRReadParams?) -> [String : Any]?](mtrclusterrvccleanmode/readattributesupportedmodes(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterrvccleanmode)*