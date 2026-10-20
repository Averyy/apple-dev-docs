# MTRClusterActions

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
class MTRClusterActions
```

```objc
@interface MTRClusterActions : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteractions/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteractions/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func disableAction(with: MTRActionsClusterDisableActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/disableaction%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func disableAction(with: MTRActionsClusterDisableActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/disableaction%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func disableActionWithDuration(with: MTRActionsClusterDisableActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/disableactionwithduration%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func disableActionWithDuration(with: MTRActionsClusterDisableActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/disableactionwithduration%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func enableAction(with: MTRActionsClusterEnableActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/enableaction%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func enableAction(with: MTRActionsClusterEnableActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/enableaction%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func enableActionWithDuration(with: MTRActionsClusterEnableActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/enableactionwithduration%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func enableActionWithDuration(with: MTRActionsClusterEnableActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/enableactionwithduration%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func instantAction(with: MTRActionsClusterInstantActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/instantaction%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func instantAction(with: MTRActionsClusterInstantActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/instantaction%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func instantActionWithTransition(with: MTRActionsClusterInstantActionWithTransitionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/instantactionwithtransition%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func instantActionWithTransition(with: MTRActionsClusterInstantActionWithTransitionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/instantactionwithtransition%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func pauseAction(with: MTRActionsClusterPauseActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/pauseaction%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func pauseAction(with: MTRActionsClusterPauseActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/pauseaction%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func pauseActionWithDuration(with: MTRActionsClusterPauseActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/pauseactionwithduration%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func pauseActionWithDuration(with: MTRActionsClusterPauseActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/pauseactionwithduration%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteractions/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActionList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteractions/readattributeactionlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteractions/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteractions/readattributeclusterrevision%28with%29.md)
- [func readAttributeEndpointLists(with: MTRReadParams?) -> [String : Any]?](./mtrclusteractions/readattributeendpointlists%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteractions/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteractions/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSetupURL(with: MTRReadParams?) -> [String : Any]?](./mtrclusteractions/readattributesetupurl%28with%29.md)
- [func resumeAction(with: MTRActionsClusterResumeActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/resumeaction%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resumeAction(with: MTRActionsClusterResumeActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/resumeaction%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func startAction(with: MTRActionsClusterStartActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/startaction%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func startAction(with: MTRActionsClusterStartActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/startaction%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func startActionWithDuration(with: MTRActionsClusterStartActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/startactionwithduration%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func startActionWithDuration(with: MTRActionsClusterStartActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/startactionwithduration%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stopAction(with: MTRActionsClusterStopActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteractions/stopaction%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stopAction(with: MTRActionsClusterStopActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteractions/stopaction%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteractions)*