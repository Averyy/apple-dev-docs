# MTRClusterIdentify

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
class MTRClusterIdentify
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteridentify/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteridentify/init(device:endpointid:queue:).md)
### Instance Methods
- [func identify(with: MTRIdentifyClusterIdentifyParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteridentify/identify(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func identify(with: MTRIdentifyClusterIdentifyParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteridentify/identify(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteridentify/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteridentify/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteridentify/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteridentify/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteridentify/readattributegeneratedcommandlist(with:).md)
- [func readAttributeIdentifyTime(with: MTRReadParams?) -> [String : Any]?](mtrclusteridentify/readattributeidentifytime(with:).md)
- [func readAttributeIdentifyType(with: MTRReadParams?) -> [String : Any]?](mtrclusteridentify/readattributeidentifytype(with:).md)
- [func triggerEffect(with: MTRIdentifyClusterTriggerEffectParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteridentify/triggereffect(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func triggerEffect(with: MTRIdentifyClusterTriggerEffectParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteridentify/triggereffect(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func writeAttributeIdentifyTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteridentify/writeattributeidentifytime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeIdentifyTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteridentify/writeattributeidentifytime(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteridentify)*