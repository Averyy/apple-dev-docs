# MTRClusterBarrierControl

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

> **Deprecated**: BarrierControl is deprecated and will be removed

## Declaration

```swift
class MTRClusterBarrierControl
```

```objc
@interface MTRClusterBarrierControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterbarriercontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterbarriercontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func barrierControlGoToPercent(with: MTRBarrierControlClusterBarrierControlGoToPercentParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterbarriercontrol/barriercontrolgotopercent%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func barrierControlGoToPercent(with: MTRBarrierControlClusterBarrierControlGoToPercentParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterbarriercontrol/barriercontrolgotopercent%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func barrierControlStop(with: MTRBarrierControlClusterBarrierControlStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterbarriercontrol/barriercontrolstop%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func barrierControlStop(with: MTRBarrierControlClusterBarrierControlStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterbarriercontrol/barriercontrolstop%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func barrierControlStop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterbarriercontrol/barriercontrolstop%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func barrierControlStop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterbarriercontrol/barriercontrolstop%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributeattributelist%28with%29.md)
- [func readAttributeBarrierCapabilities(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarriercapabilities%28with%29.md)
- [func readAttributeBarrierCloseEvents(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarriercloseevents%28with%29.md)
- [func readAttributeBarrierClosePeriod(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarriercloseperiod%28with%29.md)
- [func readAttributeBarrierCommandCloseEvents(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarriercommandcloseevents%28with%29.md)
- [func readAttributeBarrierCommandOpenEvents(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarriercommandopenevents%28with%29.md)
- [func readAttributeBarrierMovingState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarriermovingstate%28with%29.md)
- [func readAttributeBarrierOpenEvents(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarrieropenevents%28with%29.md)
- [func readAttributeBarrierOpenPeriod(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarrieropenperiod%28with%29.md)
- [func readAttributeBarrierPosition(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarrierposition%28with%29.md)
- [func readAttributeBarrierSafetyStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributebarriersafetystatus%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbarriercontrol/readattributegeneratedcommandlist%28with%29.md)
- [func writeAttributeBarrierCloseEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbarriercontrol/writeattributebarriercloseevents%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeBarrierCloseEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbarriercontrol/writeattributebarriercloseevents%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeBarrierClosePeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbarriercontrol/writeattributebarriercloseperiod%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeBarrierClosePeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbarriercontrol/writeattributebarriercloseperiod%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbarriercontrol/writeattributebarriercommandcloseevents%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbarriercontrol/writeattributebarriercommandcloseevents%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbarriercontrol/writeattributebarriercommandopenevents%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbarriercontrol/writeattributebarriercommandopenevents%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeBarrierOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbarriercontrol/writeattributebarrieropenevents%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeBarrierOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbarriercontrol/writeattributebarrieropenevents%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeBarrierOpenPeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbarriercontrol/writeattributebarrieropenperiod%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeBarrierOpenPeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbarriercontrol/writeattributebarrieropenperiod%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbarriercontrol)*