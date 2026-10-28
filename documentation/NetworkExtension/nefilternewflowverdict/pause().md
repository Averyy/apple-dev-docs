# pause()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Creates a verdict that tells the system to pause the flow.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func pause() -> NEFilterNewFlowVerdict
```

```objc
+ (NEFilterNewFlowVerdict *) pauseVerdict;
```

## Discussion

Once paused, the system doesn’t call any of the data provider’s handler callbacks until you resume the flow by calling [`resumeFlow(_:with:)`](../nefilterdataprovider/resumeflow%28_,with%29.md).

You can pause TCP flows indefinitely. You can pause UDP flows for up to 10 seconds, after which the system drops the flow. Pausing a flow that’s already paused is an invalid operation.

## See Also

### Creating new flow verdicts
- [class func allow() -> NEFilterNewFlowVerdict](./allow%28%29.md)
  Create a verdict that indicates to the system that the all of the new flow’s data should be allowed to pass to its final destination.
- [class func drop() -> NEFilterNewFlowVerdict](./drop%28%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should dropped, and the user should not be given the opportunity to request access.
- [class func filterDataVerdict(withFilterInbound: Bool, peekInboundBytes: Int, filterOutbound: Bool, peekOutboundBytes: Int) -> NEFilterNewFlowVerdict](./filterdataverdict%28withfilterinbound,peekinboundbytes,filteroutbound,peekoutboundbytes%29.md)
  Create a verdict that indicates to the system that the filter needs to make a decision about a new flow after seeing a portion of the flow’s data.
- [class func remediateVerdict(withRemediationURLMapKey: String, remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict](./remediateverdict%28withremediationurlmapkey,remediationbuttontextmapkey%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should be dropped, but allow the user to request access by tapping or clicking on a URL.
- [class func needRules() -> NEFilterNewFlowVerdict](./needrules%28%29.md)
  Create a verdict that indicates to the system that the Filter Data Provider needs more information before it can make a decision about a new flow.
- [class func urlAppendStringVerdict(withMapKey: String) -> NEFilterNewFlowVerdict](./urlappendstringverdict%28withmapkey%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should be allowed to pass to its final destination, but a string should first be appended to the new flow’s request URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/pause())*