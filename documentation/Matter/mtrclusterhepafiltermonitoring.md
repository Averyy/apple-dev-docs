# MTRClusterHEPAFilterMonitoring

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRClusterHEPAFilterMonitoring
```

```objc
@interface MTRClusterHEPAFilterMonitoring : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterhepafiltermonitoring/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributeattributelist%28with%29.md)
- [func readAttributeChangeIndication(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributechangeindication%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributeclusterrevision%28with%29.md)
- [func readAttributeCondition(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributecondition%28with%29.md)
- [func readAttributeDegradationDirection(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributedegradationdirection%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeInPlaceIndicator(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributeinplaceindicator%28with%29.md)
- [func readAttributeLastChangedTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributelastchangedtime%28with%29.md)
- [func readAttributeReplacementProductList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterhepafiltermonitoring/readattributereplacementproductlist%28with%29.md)
- [func resetCondition(with: MTRHEPAFilterMonitoringClusterResetConditionParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterhepafiltermonitoring/resetcondition%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resetCondition(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterhepafiltermonitoring/resetcondition%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributeLastChangedTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterhepafiltermonitoring/writeattributelastchangedtime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLastChangedTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterhepafiltermonitoring/writeattributelastchangedtime%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterhepafiltermonitoring)*