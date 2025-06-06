# MTRClusterHEPAFilterMonitoring

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterhepafiltermonitoring/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributeattributelist(with:).md)
- [func readAttributeChangeIndication(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributechangeindication(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributeclusterrevision(with:).md)
- [func readAttributeCondition(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributecondition(with:).md)
- [func readAttributeDegradationDirection(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributedegradationdirection(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributegeneratedcommandlist(with:).md)
- [func readAttributeInPlaceIndicator(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributeinplaceindicator(with:).md)
- [func readAttributeLastChangedTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributelastchangedtime(with:).md)
- [func readAttributeReplacementProductList(with: MTRReadParams?) -> [String : Any]?](mtrclusterhepafiltermonitoring/readattributereplacementproductlist(with:).md)
- [func resetCondition(with: MTRHEPAFilterMonitoringClusterResetConditionParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterhepafiltermonitoring/resetcondition(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resetCondition(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterhepafiltermonitoring/resetcondition(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func writeAttributeLastChangedTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterhepafiltermonitoring/writeattributelastchangedtime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLastChangedTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterhepafiltermonitoring/writeattributelastchangedtime(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterhepafiltermonitoring)*