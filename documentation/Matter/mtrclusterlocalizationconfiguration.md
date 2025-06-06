# MTRClusterLocalizationConfiguration

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
class MTRClusterLocalizationConfiguration
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterlocalizationconfiguration/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterlocalizationconfiguration/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlocalizationconfiguration/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveLocale(with: MTRReadParams?) -> [String : Any]?](mtrclusterlocalizationconfiguration/readattributeactivelocale(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlocalizationconfiguration/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterlocalizationconfiguration/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterlocalizationconfiguration/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlocalizationconfiguration/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSupportedLocales(with: MTRReadParams?) -> [String : Any]?](mtrclusterlocalizationconfiguration/readattributesupportedlocales(with:).md)
- [func writeAttributeActiveLocale(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlocalizationconfiguration/writeattributeactivelocale(withvalue:expectedvalueinterval:).md)
- [func writeAttributeActiveLocale(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlocalizationconfiguration/writeattributeactivelocale(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterlocalizationconfiguration)*