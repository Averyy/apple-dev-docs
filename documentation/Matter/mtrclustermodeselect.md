# MTRClusterModeSelect

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterModeSelect
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustermodeselect/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustermodeselect/init(device:endpointid:queue:).md)
### Instance Methods
- [func changeToMode(with: MTRModeSelectClusterChangeToModeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermodeselect/changetomode(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func changeToMode(with: MTRModeSelectClusterChangeToModeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustermodeselect/changetomode(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentMode(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributecurrentmode(with:).md)
- [func readAttributeDescription(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributedescription(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOnMode(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributeonmode(with:).md)
- [func readAttributeStandardNamespace(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributestandardnamespace(with:).md)
- [func readAttributeStartUpMode(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributestartupmode(with:).md)
- [func readAttributeSupportedModes(with: MTRReadParams?) -> [String : Any]?](mtrclustermodeselect/readattributesupportedmodes(with:).md)
- [func writeAttributeOnMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustermodeselect/writeattributeonmode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOnMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustermodeselect/writeattributeonmode(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeStartUpMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustermodeselect/writeattributestartupmode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeStartUpMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustermodeselect/writeattributestartupmode(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermodeselect)*