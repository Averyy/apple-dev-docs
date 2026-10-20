# remediateVerdict(withRemediationURLMapKey:remediationButtonTextMapKey:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Create a verdict that indicates to the system that all of the new flow’s data should be dropped, but allow the user to request access by tapping or clicking on a URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func remediateVerdict(withRemediationURLMapKey remediationURLMapKey: String, remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict
```

```objc
+ (NEFilterNewFlowVerdict *) remediateVerdictWithRemediationURLMapKey:(NSString *) remediationURLMapKey remediationButtonTextMapKey:(NSString *) remediationButtonTextMapKey;
```

#### Return Value

An `NEFilterNewFlowVerdict` object.

#### Discussion

When the Filter Data Provider returns this verdict from its `handleNewFlow:` method, the system uses the verdict’s `remediationURLMapKey` and `remediationButtonTextMapKey` to look up the remediation URL parameters in the [`remediationMap`](../nefiltercontrolprovider/remediationmap.md) dictionary set by the Filter Control Provider. The remediation URL parameters are then inserted into the block page which is presented to the user.

## Parameters

- `remediationURLMapKey`: The key in the Filter Control Provider’s [`remediationMap`](../nefiltercontrolprovider/remediationmap.md) dictionary corresponding to the URL of the remediation link to give to the user.
- `remediationButtonTextMapKey`: The key in the Filter Control Provider’s [`remediationMap`](../nefiltercontrolprovider/remediationmap.md) dictionary corresponding to the text of the remediation link text to give to the user.

## See Also

### Creating new flow verdicts
- [class func allow() -> NEFilterNewFlowVerdict](./allow%28%29.md)
  Create a verdict that indicates to the system that the all of the new flow’s data should be allowed to pass to its final destination.
- [class func drop() -> NEFilterNewFlowVerdict](./drop%28%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should dropped, and the user should not be given the opportunity to request access.
- [class func pause() -> NEFilterNewFlowVerdict](./pause%28%29.md)
  Creates a verdict that tells the system to pause the flow.
- [class func filterDataVerdict(withFilterInbound: Bool, peekInboundBytes: Int, filterOutbound: Bool, peekOutboundBytes: Int) -> NEFilterNewFlowVerdict](./filterdataverdict%28withfilterinbound,peekinboundbytes,filteroutbound,peekoutboundbytes%29.md)
  Create a verdict that indicates to the system that the filter needs to make a decision about a new flow after seeing a portion of the flow’s data.
- [class func needRules() -> NEFilterNewFlowVerdict](./needrules%28%29.md)
  Create a verdict that indicates to the system that the Filter Data Provider needs more information before it can make a decision about a new flow.
- [class func urlAppendStringVerdict(withMapKey: String) -> NEFilterNewFlowVerdict](./urlappendstringverdict%28withmapkey%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should be allowed to pass to its final destination, but a string should first be appended to the new flow’s request URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/remediateverdict(withremediationurlmapkey:remediationbuttontextmapkey:))*