# MTRClusterOnOff

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
class MTRClusterOnOff
```

```objc
@interface MTRClusterOnOff : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteronoff/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteronoff/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func off(with: MTROnOffClusterOffParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/off%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func off(with: MTROnOffClusterOffParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/off%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func off(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/off%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func off(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/off%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func offWithEffect(with: MTROnOffClusterOffWithEffectParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/offwitheffect%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func offWithEffect(with: MTROnOffClusterOffWithEffectParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/offwitheffect%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func on(with: MTROnOffClusterOnParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/on%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func on(with: MTROnOffClusterOnParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/on%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func on(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/on%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func on(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/on%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func onWithRecallGlobalScene(with: MTROnOffClusterOnWithRecallGlobalSceneParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/onwithrecallglobalscene%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func onWithRecallGlobalScene(with: MTROnOffClusterOnWithRecallGlobalSceneParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/onwithrecallglobalscene%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func onWithRecallGlobalScene(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/onwithrecallglobalscene%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func onWithRecallGlobalScene(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/onwithrecallglobalscene%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func onWithTimedOff(with: MTROnOffClusterOnWithTimedOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/onwithtimedoff%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func onWithTimedOff(with: MTROnOffClusterOnWithTimedOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/onwithtimedoff%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeGlobalSceneControl(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributeglobalscenecontrol%28with%29.md)
- [func readAttributeOffWaitTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributeoffwaittime%28with%29.md)
- [func readAttributeOnOff(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributeonoff%28with%29.md)
- [func readAttributeOnTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributeontime%28with%29.md)
- [func readAttributeStartUp(with: MTRReadParams?) -> [String : Any]?](./mtrclusteronoff/readattributestartup%28with%29.md)
- [func toggle(with: MTROnOffClusterToggleParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/toggle%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func toggle(with: MTROnOffClusterToggleParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/toggle%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func toggle(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteronoff/toggle%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func toggle(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteronoff/toggle%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func writeAttributeOffWaitTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteronoff/writeattributeoffwaittime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOffWaitTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteronoff/writeattributeoffwaittime%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOnTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteronoff/writeattributeontime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOnTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteronoff/writeattributeontime%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeStartUp(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteronoff/writeattributestartup%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeStartUp(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteronoff/writeattributestartup%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteronoff)*