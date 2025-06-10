# MTRClusterLevelControl

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
class MTRClusterLevelControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterlevelcontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterlevelcontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func move(with: MTRLevelControlClusterMoveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/move(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func move(with: MTRLevelControlClusterMoveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/move(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveToClosestFrequency(with: MTRLevelControlClusterMoveToClosestFrequencyParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/movetoclosestfrequency(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveToClosestFrequency(with: MTRLevelControlClusterMoveToClosestFrequencyParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/movetoclosestfrequency(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveToLevel(with: MTRLevelControlClusterMoveToLevelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/movetolevel(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveToLevel(with: MTRLevelControlClusterMoveToLevelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/movetolevel(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveToLevelWithOnOff(with: MTRLevelControlClusterMoveToLevelWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/movetolevelwithonoff(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveToLevelWithOnOff(with: MTRLevelControlClusterMoveToLevelWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/movetolevelwithonoff(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func moveWithOnOff(with: MTRLevelControlClusterMoveWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/movewithonoff(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func moveWithOnOff(with: MTRLevelControlClusterMoveWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/movewithonoff(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentFrequency(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributecurrentfrequency(with:).md)
- [func readAttributeCurrentLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributecurrentlevel(with:).md)
- [func readAttributeDefaultMoveRate(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributedefaultmoverate(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributeMaxFrequency(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributemaxfrequency(with:).md)
- [func readAttributeMaxLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributemaxlevel(with:).md)
- [func readAttributeMinFrequency(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeminfrequency(with:).md)
- [func readAttributeMinLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeminlevel(with:).md)
- [func readAttributeOffTransitionTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeofftransitiontime(with:).md)
- [func readAttributeOnLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeonlevel(with:).md)
- [func readAttributeOnOffTransitionTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeonofftransitiontime(with:).md)
- [func readAttributeOnTransitionTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeontransitiontime(with:).md)
- [func readAttributeOptions(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeoptions(with:).md)
- [func readAttributeRemainingTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributeremainingtime(with:).md)
- [func readAttributeStartUpCurrentLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterlevelcontrol/readattributestartupcurrentlevel(with:).md)
- [func step(with: MTRLevelControlClusterStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/step(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func step(with: MTRLevelControlClusterStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/step(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stepWithOnOff(with: MTRLevelControlClusterStepWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/stepwithonoff(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stepWithOnOff(with: MTRLevelControlClusterStepWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/stepwithonoff(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stop(with: MTRLevelControlClusterStopParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/stop(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stop(with: MTRLevelControlClusterStopParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/stop(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stopWithOnOff(with: MTRLevelControlClusterStopWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterlevelcontrol/stopwithonoff(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stopWithOnOff(with: MTRLevelControlClusterStopWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterlevelcontrol/stopwithonoff(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func writeAttributeDefaultMoveRate(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlevelcontrol/writeattributedefaultmoverate(withvalue:expectedvalueinterval:).md)
- [func writeAttributeDefaultMoveRate(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlevelcontrol/writeattributedefaultmoverate(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOffTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlevelcontrol/writeattributeofftransitiontime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOffTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlevelcontrol/writeattributeofftransitiontime(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOnLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlevelcontrol/writeattributeonlevel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOnLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlevelcontrol/writeattributeonlevel(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOnOffTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlevelcontrol/writeattributeonofftransitiontime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOnOffTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlevelcontrol/writeattributeonofftransitiontime(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOnTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlevelcontrol/writeattributeontransitiontime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOnTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlevelcontrol/writeattributeontransitiontime(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOptions(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlevelcontrol/writeattributeoptions(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOptions(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlevelcontrol/writeattributeoptions(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeStartUpCurrentLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlevelcontrol/writeattributestartupcurrentlevel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeStartUpCurrentLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlevelcontrol/writeattributestartupcurrentlevel(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterlevelcontrol)*