# MTRClusterOnOffSwitchConfiguration

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

> **Deprecated**: OnOffSwitchConfiguration is deprecated and will be removed

## Declaration

```swift
class MTRClusterOnOffSwitchConfiguration
```

```objc
@interface MTRClusterOnOffSwitchConfiguration : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteronoffswitchconfiguration/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteronoffswitchconfiguration/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoffswitchconfiguration/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoffswitchconfiguration/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoffswitchconfiguration/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoffswitchconfiguration/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoffswitchconfiguration/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSwitchActions(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoffswitchconfiguration/readattributeswitchactions%28with%29.md)
- [func readAttributeSwitchType(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoffswitchconfiguration/readattributeswitchtype%28with%29.md)
- [func writeAttributeSwitchActions(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteronoffswitchconfiguration/writeattributeswitchactions%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSwitchActions(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteronoffswitchconfiguration/writeattributeswitchactions%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteronoffswitchconfiguration)*