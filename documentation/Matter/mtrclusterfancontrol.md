# MTRClusterFanControl

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
class MTRClusterFanControl
```

```objc
@interface MTRClusterFanControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterfancontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterfancontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAirflowDirection(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributeairflowdirection%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeFanMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributefanmode%28with%29.md)
- [func readAttributeFanModeSequence(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributefanmodesequence%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributePercentCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributepercentcurrent%28with%29.md)
- [func readAttributePercentSetting(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributepercentsetting%28with%29.md)
- [func readAttributeRockSetting(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributerocksetting%28with%29.md)
- [func readAttributeRockSupport(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributerocksupport%28with%29.md)
- [func readAttributeSpeedCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributespeedcurrent%28with%29.md)
- [func readAttributeSpeedMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributespeedmax%28with%29.md)
- [func readAttributeSpeedSetting(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributespeedsetting%28with%29.md)
- [func readAttributeWindSetting(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributewindsetting%28with%29.md)
- [func readAttributeWindSupport(with: MTRReadParams?) -> [String : Any]?](./mtrclusterfancontrol/readattributewindsupport%28with%29.md)
- [func step(with: MTRFanControlClusterStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterfancontrol/step%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributeAirflowDirection(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterfancontrol/writeattributeairflowdirection%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeAirflowDirection(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterfancontrol/writeattributeairflowdirection%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeFanMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterfancontrol/writeattributefanmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeFanMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterfancontrol/writeattributefanmode%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeFanModeSequence(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterfancontrol/writeattributefanmodesequence%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeFanModeSequence(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterfancontrol/writeattributefanmodesequence%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributePercentSetting(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterfancontrol/writeattributepercentsetting%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributePercentSetting(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterfancontrol/writeattributepercentsetting%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeRockSetting(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterfancontrol/writeattributerocksetting%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeRockSetting(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterfancontrol/writeattributerocksetting%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeSpeedSetting(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterfancontrol/writeattributespeedsetting%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSpeedSetting(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterfancontrol/writeattributespeedsetting%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeWindSetting(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterfancontrol/writeattributewindsetting%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeWindSetting(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterfancontrol/writeattributewindsetting%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterfancontrol)*