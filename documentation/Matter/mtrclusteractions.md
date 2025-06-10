# MTRClusterActions

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
class MTRClusterActions
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteractions/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteractions/init(device:endpointid:queue:).md)
### Instance Methods
- [func disableAction(with: MTRActionsClusterDisableActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/disableaction(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func disableAction(with: MTRActionsClusterDisableActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/disableaction(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func disableActionWithDuration(with: MTRActionsClusterDisableActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/disableactionwithduration(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func disableActionWithDuration(with: MTRActionsClusterDisableActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/disableactionwithduration(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func enableAction(with: MTRActionsClusterEnableActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/enableaction(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func enableAction(with: MTRActionsClusterEnableActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/enableaction(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func enableActionWithDuration(with: MTRActionsClusterEnableActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/enableactionwithduration(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func enableActionWithDuration(with: MTRActionsClusterEnableActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/enableactionwithduration(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func instantAction(with: MTRActionsClusterInstantActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/instantaction(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func instantAction(with: MTRActionsClusterInstantActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/instantaction(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func instantActionWithTransition(with: MTRActionsClusterInstantActionWithTransitionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/instantactionwithtransition(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func instantActionWithTransition(with: MTRActionsClusterInstantActionWithTransitionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/instantactionwithtransition(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func pauseAction(with: MTRActionsClusterPauseActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/pauseaction(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func pauseAction(with: MTRActionsClusterPauseActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/pauseaction(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func pauseActionWithDuration(with: MTRActionsClusterPauseActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/pauseactionwithduration(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func pauseActionWithDuration(with: MTRActionsClusterPauseActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/pauseactionwithduration(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteractions/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActionList(with: MTRReadParams?) -> [String : Any]?](mtrclusteractions/readattributeactionlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteractions/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteractions/readattributeclusterrevision(with:).md)
- [func readAttributeEndpointLists(with: MTRReadParams?) -> [String : Any]?](mtrclusteractions/readattributeendpointlists(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteractions/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteractions/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSetupURL(with: MTRReadParams?) -> [String : Any]?](mtrclusteractions/readattributesetupurl(with:).md)
- [func resumeAction(with: MTRActionsClusterResumeActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/resumeaction(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resumeAction(with: MTRActionsClusterResumeActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/resumeaction(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func startAction(with: MTRActionsClusterStartActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/startaction(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func startAction(with: MTRActionsClusterStartActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/startaction(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func startActionWithDuration(with: MTRActionsClusterStartActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/startactionwithduration(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func startActionWithDuration(with: MTRActionsClusterStartActionWithDurationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/startactionwithduration(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stopAction(with: MTRActionsClusterStopActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteractions/stopaction(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stopAction(with: MTRActionsClusterStopActionParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteractions/stopaction(with:expectedvalues:expectedvalueinterval:completionhandler:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteractions)*