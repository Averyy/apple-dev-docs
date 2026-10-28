# urlAppendStringVerdict(withMapKey:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Create a verdict that indicates to the system that all of the new flow’s data should be allowed to pass to its final destination, but a string should first be appended to the new flow’s request URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func urlAppendStringVerdict(withMapKey urlAppendMapKey: String) -> NEFilterNewFlowVerdict
```

```objc
+ (NEFilterNewFlowVerdict *) URLAppendStringVerdictWithMapKey:(NSString *) urlAppendMapKey;
```

## Return Value

A `NEFilterNewFlowVerdict` object.

## Parameters

- `urlAppendMapKey`: The key in the Filter Control Provider’s [`urlAppendStringMap`](../nefiltercontrolprovider/urlappendstringmap.md) dictionary corresponding to the string to append to the new flow’s request URL.

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
- [class func remediateVerdict(withRemediationURLMapKey: String, remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict](./remediateverdict%28withremediationurlmapkey,remediationbuttontextmapkey%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should be dropped, but allow the user to request access by tapping or clicking on a URL.
- [class func needRules() -> NEFilterNewFlowVerdict](./needrules%28%29.md)
  Create a verdict that indicates to the system that the Filter Data Provider needs more information before it can make a decision about a new flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/urlappendstringverdict(withmapkey:))*