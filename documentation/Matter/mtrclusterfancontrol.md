# MTRClusterFanControl

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
class MTRClusterFanControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterfancontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterfancontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAirflowDirection(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributeairflowdirection(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributeclusterrevision(with:).md)
- [func readAttributeFanMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributefanmode(with:).md)
- [func readAttributeFanModeSequence(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributefanmodesequence(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributePercentCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributepercentcurrent(with:).md)
- [func readAttributePercentSetting(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributepercentsetting(with:).md)
- [func readAttributeRockSetting(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributerocksetting(with:).md)
- [func readAttributeRockSupport(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributerocksupport(with:).md)
- [func readAttributeSpeedCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributespeedcurrent(with:).md)
- [func readAttributeSpeedMax(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributespeedmax(with:).md)
- [func readAttributeSpeedSetting(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributespeedsetting(with:).md)
- [func readAttributeWindSetting(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributewindsetting(with:).md)
- [func readAttributeWindSupport(with: MTRReadParams?) -> [String : Any]?](mtrclusterfancontrol/readattributewindsupport(with:).md)
- [func step(with: MTRFanControlClusterStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterfancontrol/step(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func writeAttributeAirflowDirection(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterfancontrol/writeattributeairflowdirection(withvalue:expectedvalueinterval:).md)
- [func writeAttributeAirflowDirection(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterfancontrol/writeattributeairflowdirection(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeFanMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterfancontrol/writeattributefanmode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeFanMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterfancontrol/writeattributefanmode(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeFanModeSequence(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterfancontrol/writeattributefanmodesequence(withvalue:expectedvalueinterval:).md)
- [func writeAttributeFanModeSequence(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterfancontrol/writeattributefanmodesequence(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributePercentSetting(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterfancontrol/writeattributepercentsetting(withvalue:expectedvalueinterval:).md)
- [func writeAttributePercentSetting(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterfancontrol/writeattributepercentsetting(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeRockSetting(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterfancontrol/writeattributerocksetting(withvalue:expectedvalueinterval:).md)
- [func writeAttributeRockSetting(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterfancontrol/writeattributerocksetting(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeSpeedSetting(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterfancontrol/writeattributespeedsetting(withvalue:expectedvalueinterval:).md)
- [func writeAttributeSpeedSetting(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterfancontrol/writeattributespeedsetting(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeWindSetting(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterfancontrol/writeattributewindsetting(withvalue:expectedvalueinterval:).md)
- [func writeAttributeWindSetting(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterfancontrol/writeattributewindsetting(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterfancontrol)*