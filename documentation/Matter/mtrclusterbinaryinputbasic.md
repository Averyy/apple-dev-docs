# MTRClusterBinaryInputBasic

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 18.2
- iPadOS 16.1+ - Deprecated in 18.2
- Mac Catalyst 16.1+ - Deprecated in 18.2
- macOS 13.0+ - Deprecated in 15.2
- tvOS 16.1+ - Deprecated in 18.2
- visionOS 1.0+ - Deprecated in 2.2
- watchOS 9.1+ - Deprecated in 11.2

> **Deprecated**: BinaryInputBasic is deprecated and will be removed

## Declaration

```swift
class MTRClusterBinaryInputBasic
```

```objc
@interface MTRClusterBinaryInputBasic : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterbinaryinputbasic/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterbinaryinputbasic/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveText(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributeactivetext%28with%29.md)
- [func readAttributeApplicationType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributeapplicationtype%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributeclusterrevision%28with%29.md)
- [func readAttributeDescription(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributedescription%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeInactiveText(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributeinactivetext%28with%29.md)
- [func readAttributeOutOfService(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributeoutofservice%28with%29.md)
- [func readAttributePolarity(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributepolarity%28with%29.md)
- [func readAttributePresentValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributepresentvalue%28with%29.md)
- [func readAttributeReliability(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributereliability%28with%29.md)
- [func readAttributeStatusFlags(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbinaryinputbasic/readattributestatusflags%28with%29.md)
- [func writeAttributeActiveText(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbinaryinputbasic/writeattributeactivetext%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeActiveText(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbinaryinputbasic/writeattributeactivetext%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeDescription(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbinaryinputbasic/writeattributedescription%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeDescription(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbinaryinputbasic/writeattributedescription%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeInactiveText(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbinaryinputbasic/writeattributeinactivetext%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeInactiveText(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbinaryinputbasic/writeattributeinactivetext%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOutOfService(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbinaryinputbasic/writeattributeoutofservice%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOutOfService(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbinaryinputbasic/writeattributeoutofservice%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributePresentValue(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbinaryinputbasic/writeattributepresentvalue%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributePresentValue(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbinaryinputbasic/writeattributepresentvalue%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeReliability(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbinaryinputbasic/writeattributereliability%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeReliability(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbinaryinputbasic/writeattributereliability%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbinaryinputbasic)*