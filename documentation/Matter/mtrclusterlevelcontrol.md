# MTRClusterLevelControl

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
class MTRClusterLevelControl
```

```objc
@interface MTRClusterLevelControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterlevelcontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterlevelcontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func move(with: MTRLevelControlClusterMoveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/move%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func move(with: MTRLevelControlClusterMoveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/move%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveToClosestFrequency(with: MTRLevelControlClusterMoveToClosestFrequencyParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/movetoclosestfrequency%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveToClosestFrequency(with: MTRLevelControlClusterMoveToClosestFrequencyParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/movetoclosestfrequency%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveToLevel(with: MTRLevelControlClusterMoveToLevelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/movetolevel%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveToLevel(with: MTRLevelControlClusterMoveToLevelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/movetolevel%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveToLevelWithOnOff(with: MTRLevelControlClusterMoveToLevelWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/movetolevelwithonoff%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveToLevelWithOnOff(with: MTRLevelControlClusterMoveToLevelWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/movetolevelwithonoff%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveWithOnOff(with: MTRLevelControlClusterMoveWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/movewithonoff%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveWithOnOff(with: MTRLevelControlClusterMoveWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/movewithonoff%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentFrequency(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributecurrentfrequency%28with%29.md)
- [func readAttributeCurrentLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributecurrentlevel%28with%29.md)
- [func readAttributeDefaultMoveRate(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributedefaultmoverate%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeMaxFrequency(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributemaxfrequency%28with%29.md)
- [func readAttributeMaxLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributemaxlevel%28with%29.md)
- [func readAttributeMinFrequency(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeminfrequency%28with%29.md)
- [func readAttributeMinLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeminlevel%28with%29.md)
- [func readAttributeOffTransitionTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeofftransitiontime%28with%29.md)
- [func readAttributeOnLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeonlevel%28with%29.md)
- [func readAttributeOnOffTransitionTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeonofftransitiontime%28with%29.md)
- [func readAttributeOnTransitionTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeontransitiontime%28with%29.md)
- [func readAttributeOptions(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeoptions%28with%29.md)
- [func readAttributeRemainingTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributeremainingtime%28with%29.md)
- [func readAttributeStartUpCurrentLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlevelcontrol/readattributestartupcurrentlevel%28with%29.md)
- [func step(with: MTRLevelControlClusterStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/step%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func step(with: MTRLevelControlClusterStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/step%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stepWithOnOff(with: MTRLevelControlClusterStepWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/stepwithonoff%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stepWithOnOff(with: MTRLevelControlClusterStepWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/stepwithonoff%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stop(with: MTRLevelControlClusterStopParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/stop%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stop(with: MTRLevelControlClusterStopParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/stop%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stopWithOnOff(with: MTRLevelControlClusterStopWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/stopwithonoff%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stopWithOnOff(with: MTRLevelControlClusterStopWithOnOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterlevelcontrol/stopwithonoff%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func writeAttributeDefaultMoveRate(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlevelcontrol/writeattributedefaultmoverate%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeDefaultMoveRate(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlevelcontrol/writeattributedefaultmoverate%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOffTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlevelcontrol/writeattributeofftransitiontime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOffTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlevelcontrol/writeattributeofftransitiontime%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOnLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlevelcontrol/writeattributeonlevel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOnLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlevelcontrol/writeattributeonlevel%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOnOffTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlevelcontrol/writeattributeonofftransitiontime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOnOffTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlevelcontrol/writeattributeonofftransitiontime%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOnTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlevelcontrol/writeattributeontransitiontime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOnTransitionTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlevelcontrol/writeattributeontransitiontime%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOptions(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlevelcontrol/writeattributeoptions%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOptions(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlevelcontrol/writeattributeoptions%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeStartUpCurrentLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlevelcontrol/writeattributestartupcurrentlevel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeStartUpCurrentLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlevelcontrol/writeattributestartupcurrentlevel%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterlevelcontrol)*