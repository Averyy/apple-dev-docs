# MTRClusterOnOff

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
class MTRClusterOnOff
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteronoff/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteronoff/init(device:endpointid:queue:).md)
### Instance Methods
- [func off(with: MTROnOffClusterOffParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/off(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func off(with: MTROnOffClusterOffParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/off(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func off(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/off(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func off(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/off(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func offWithEffect(with: MTROnOffClusterOffWithEffectParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/offwitheffect(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func offWithEffect(with: MTROnOffClusterOffWithEffectParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/offwitheffect(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func on(with: MTROnOffClusterOnParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/on(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func on(with: MTROnOffClusterOnParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/on(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func on(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/on(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func on(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/on(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func onWithRecallGlobalScene(with: MTROnOffClusterOnWithRecallGlobalSceneParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/onwithrecallglobalscene(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func onWithRecallGlobalScene(with: MTROnOffClusterOnWithRecallGlobalSceneParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/onwithrecallglobalscene(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func onWithRecallGlobalScene(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/onwithrecallglobalscene(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func onWithRecallGlobalScene(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/onwithrecallglobalscene(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func onWithTimedOff(with: MTROnOffClusterOnWithTimedOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/onwithtimedoff(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func onWithTimedOff(with: MTROnOffClusterOnWithTimedOffParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/onwithtimedoff(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributegeneratedcommandlist(with:).md)
- [func readAttributeGlobalSceneControl(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributeglobalscenecontrol(with:).md)
- [func readAttributeOffWaitTime(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributeoffwaittime(with:).md)
- [func readAttributeOnOff(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributeonoff(with:).md)
- [func readAttributeOnTime(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributeontime(with:).md)
- [func readAttributeStartUp(with: MTRReadParams?) -> [String : Any]?](mtrclusteronoff/readattributestartup(with:).md)
- [func toggle(with: MTROnOffClusterToggleParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/toggle(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func toggle(with: MTROnOffClusterToggleParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/toggle(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func toggle(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteronoff/toggle(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func toggle(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteronoff/toggle(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func writeAttributeOffWaitTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteronoff/writeattributeoffwaittime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOffWaitTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteronoff/writeattributeoffwaittime(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOnTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteronoff/writeattributeontime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOnTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteronoff/writeattributeontime(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeStartUp(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteronoff/writeattributestartup(withvalue:expectedvalueinterval:).md)
- [func writeAttributeStartUp(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteronoff/writeattributestartup(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteronoff)*