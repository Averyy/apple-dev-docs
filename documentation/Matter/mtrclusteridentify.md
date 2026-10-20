# MTRClusterIdentify

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterIdentify : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteridentify/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteridentify/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func identify(with: MTRIdentifyClusterIdentifyParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteridentify/identify%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func identify(with: MTRIdentifyClusterIdentifyParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteridentify/identify%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteridentify/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteridentify/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteridentify/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteridentify/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteridentify/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeIdentifyTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusteridentify/readattributeidentifytime%28with%29.md)
- [func readAttributeIdentifyType(with: MTRReadParams?) -> [String : Any]?](./mtrclusteridentify/readattributeidentifytype%28with%29.md)
- [func triggerEffect(with: MTRIdentifyClusterTriggerEffectParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteridentify/triggereffect%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func triggerEffect(with: MTRIdentifyClusterTriggerEffectParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteridentify/triggereffect%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func writeAttributeIdentifyTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteridentify/writeattributeidentifytime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeIdentifyTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteridentify/writeattributeidentifytime%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteridentify)*