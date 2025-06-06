# MTRClusterBinaryInputBasic

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
class MTRClusterBinaryInputBasic
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterbinaryinputbasic/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterbinaryinputbasic/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveText(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributeactivetext(with:).md)
- [func readAttributeApplicationType(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributeapplicationtype(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributeclusterrevision(with:).md)
- [func readAttributeDescription(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributedescription(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributegeneratedcommandlist(with:).md)
- [func readAttributeInactiveText(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributeinactivetext(with:).md)
- [func readAttributeOutOfService(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributeoutofservice(with:).md)
- [func readAttributePolarity(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributepolarity(with:).md)
- [func readAttributePresentValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributepresentvalue(with:).md)
- [func readAttributeReliability(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributereliability(with:).md)
- [func readAttributeStatusFlags(with: MTRReadParams?) -> [String : Any]?](mtrclusterbinaryinputbasic/readattributestatusflags(with:).md)
- [func writeAttributeActiveText(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbinaryinputbasic/writeattributeactivetext(withvalue:expectedvalueinterval:).md)
- [func writeAttributeActiveText(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbinaryinputbasic/writeattributeactivetext(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeDescription(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbinaryinputbasic/writeattributedescription(withvalue:expectedvalueinterval:).md)
- [func writeAttributeDescription(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbinaryinputbasic/writeattributedescription(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeInactiveText(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbinaryinputbasic/writeattributeinactivetext(withvalue:expectedvalueinterval:).md)
- [func writeAttributeInactiveText(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbinaryinputbasic/writeattributeinactivetext(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOutOfService(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbinaryinputbasic/writeattributeoutofservice(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOutOfService(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbinaryinputbasic/writeattributeoutofservice(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributePresentValue(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbinaryinputbasic/writeattributepresentvalue(withvalue:expectedvalueinterval:).md)
- [func writeAttributePresentValue(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbinaryinputbasic/writeattributepresentvalue(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeReliability(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbinaryinputbasic/writeattributereliability(withvalue:expectedvalueinterval:).md)
- [func writeAttributeReliability(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbinaryinputbasic/writeattributereliability(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbinaryinputbasic)*