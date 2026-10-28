# filterDataVerdict(withFilterInbound:peekInboundBytes:filterOutbound:peekOutboundBytes:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Create a verdict that indicates to the system that the filter needs to make a decision about a new flow after seeing a portion of the flow’s data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func filterDataVerdict(withFilterInbound filterInbound: Bool, peekInboundBytes: Int, filterOutbound: Bool, peekOutboundBytes: Int) -> NEFilterNewFlowVerdict
```

```objc
+ (NEFilterNewFlowVerdict *) filterDataVerdictWithFilterInbound:(BOOL) filterInbound peekInboundBytes:(NSUInteger) peekInboundBytes filterOutbound:(BOOL) filterOutbound peekOutboundBytes:(NSUInteger) peekOutboundBytes;
```

## Return Value

A `NEFilterNewFlowVerdict` object.

## Parameters

- `filterInbound`: A Boolean indicating whether or not the filter needs to see inbound data for the flow.
- `peekInboundBytes`: The number of inbound bytes that the filter needs to see in the subsequent call to -[[`NEFilterDataProvider`](../nefilterdataprovider.md) `handleInboundDataFromFlow:readBytesStartOffset:readBytes:`].
- `filterOutbound`: A Boolean indicating whether or not the filter needs to see outbound data for the flow.
- `peekOutboundBytes`: The number of outbound bytes that the filter needs to see in the subsequent call to -[[`NEFilterDataProvider`](../nefilterdataprovider.md) `handleOutboundDataFromFlow:readBytesStartOffset:readBytes`:].

## See Also

### Creating new flow verdicts
- [class func allow() -> NEFilterNewFlowVerdict](./allow%28%29.md)
  Create a verdict that indicates to the system that the all of the new flow’s data should be allowed to pass to its final destination.
- [class func drop() -> NEFilterNewFlowVerdict](./drop%28%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should dropped, and the user should not be given the opportunity to request access.
- [class func pause() -> NEFilterNewFlowVerdict](./pause%28%29.md)
  Creates a verdict that tells the system to pause the flow.
- [class func remediateVerdict(withRemediationURLMapKey: String, remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict](./remediateverdict%28withremediationurlmapkey,remediationbuttontextmapkey%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should be dropped, but allow the user to request access by tapping or clicking on a URL.
- [class func needRules() -> NEFilterNewFlowVerdict](./needrules%28%29.md)
  Create a verdict that indicates to the system that the Filter Data Provider needs more information before it can make a decision about a new flow.
- [class func urlAppendStringVerdict(withMapKey: String) -> NEFilterNewFlowVerdict](./urlappendstringverdict%28withmapkey%29.md)
  Create a verdict that indicates to the system that all of the new flow’s data should be allowed to pass to its final destination, but a string should first be appended to the new flow’s request URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/filterdataverdict(withfilterinbound:peekinboundbytes:filteroutbound:peekoutboundbytes:))*