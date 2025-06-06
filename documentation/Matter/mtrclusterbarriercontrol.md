# MTRClusterBarrierControl

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
class MTRClusterBarrierControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterbarriercontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterbarriercontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func barrierControlGoToPercent(with: MTRBarrierControlClusterBarrierControlGoToPercentParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterbarriercontrol/barriercontrolgotopercent(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func barrierControlGoToPercent(with: MTRBarrierControlClusterBarrierControlGoToPercentParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterbarriercontrol/barriercontrolgotopercent(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func barrierControlStop(with: MTRBarrierControlClusterBarrierControlStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterbarriercontrol/barriercontrolstop(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func barrierControlStop(with: MTRBarrierControlClusterBarrierControlStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterbarriercontrol/barriercontrolstop(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func barrierControlStop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterbarriercontrol/barriercontrolstop(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func barrierControlStop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterbarriercontrol/barriercontrolstop(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributeattributelist(with:).md)
- [func readAttributeBarrierCapabilities(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarriercapabilities(with:).md)
- [func readAttributeBarrierCloseEvents(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarriercloseevents(with:).md)
- [func readAttributeBarrierClosePeriod(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarriercloseperiod(with:).md)
- [func readAttributeBarrierCommandCloseEvents(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarriercommandcloseevents(with:).md)
- [func readAttributeBarrierCommandOpenEvents(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarriercommandopenevents(with:).md)
- [func readAttributeBarrierMovingState(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarriermovingstate(with:).md)
- [func readAttributeBarrierOpenEvents(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarrieropenevents(with:).md)
- [func readAttributeBarrierOpenPeriod(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarrieropenperiod(with:).md)
- [func readAttributeBarrierPosition(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarrierposition(with:).md)
- [func readAttributeBarrierSafetyStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributebarriersafetystatus(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbarriercontrol/readattributegeneratedcommandlist(with:).md)
- [func writeAttributeBarrierCloseEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbarriercontrol/writeattributebarriercloseevents(withvalue:expectedvalueinterval:).md)
- [func writeAttributeBarrierCloseEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbarriercontrol/writeattributebarriercloseevents(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeBarrierClosePeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbarriercontrol/writeattributebarriercloseperiod(withvalue:expectedvalueinterval:).md)
- [func writeAttributeBarrierClosePeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbarriercontrol/writeattributebarriercloseperiod(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbarriercontrol/writeattributebarriercommandcloseevents(withvalue:expectedvalueinterval:).md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbarriercontrol/writeattributebarriercommandcloseevents(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbarriercontrol/writeattributebarriercommandopenevents(withvalue:expectedvalueinterval:).md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbarriercontrol/writeattributebarriercommandopenevents(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeBarrierOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbarriercontrol/writeattributebarrieropenevents(withvalue:expectedvalueinterval:).md)
- [func writeAttributeBarrierOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbarriercontrol/writeattributebarrieropenevents(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeBarrierOpenPeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbarriercontrol/writeattributebarrieropenperiod(withvalue:expectedvalueinterval:).md)
- [func writeAttributeBarrierOpenPeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbarriercontrol/writeattributebarrieropenperiod(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbarriercontrol)*