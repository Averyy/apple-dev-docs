# filterDataVerdict(withFilterInbound:peekInboundBytes:filterOutbound:peekOutboundBytes:)

**Framework**: Network Extension  
**Kind**: method

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

#### Return Value

A `NEFilterNewFlowVerdict` object.

## Parameters

- `filterInbound`: A Boolean indicating whether or not the filter needs to see inbound data for the flow.
- `peekInboundBytes`: The number of inbound bytes that the filter needs to see in the subsequent call to -[   ].
- `filterOutbound`: A Boolean indicating whether or not the filter needs to see outbound data for the flow.
- `peekOutboundBytes`: The number of outbound bytes that the filter needs to see in the subsequent call to -[   :].

## See Also

- [class func allow() -> NEFilterNewFlowVerdict](nefilternewflowverdict/allow.md)
  Create a verdict that indicates to the system that the all of the new flow’s data should be allowed to pass to its final destination.
- [class func drop() -> NEFilterNewFlowVerdict](nefilternewflowverdict/drop.md)
  Create a verdict that indicates to the system that all of the new flow’s data should dropped, and the user should not be given the opportunity to request access.
- [class func pause() -> NEFilterNewFlowVerdict](nefilternewflowverdict/pause.md)
  Creates a verdict that tells the system to pause the flow.
- [class func remediateVerdict(withRemediationURLMapKey: String, remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict](nefilternewflowverdict/remediateverdict(withremediationurlmapkey:remediationbuttontextmapkey:).md)
  Create a verdict that indicates to the system that all of the new flow’s data should be dropped, but allow the user to request access by tapping or clicking on a URL.
- [class func needRules() -> NEFilterNewFlowVerdict](nefilternewflowverdict/needrules.md)
  Create a verdict that indicates to the system that the Filter Data Provider needs more information before it can make a decision about a new flow.
- [class func urlAppendStringVerdict(withMapKey: String) -> NEFilterNewFlowVerdict](nefilternewflowverdict/urlappendstringverdict(withmapkey:).md)
  Create a verdict that indicates to the system that all of the new flow’s data should be allowed to pass to its final destination, but a string should first be appended to the new flow’s request URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/filterdataverdict(withfilterinbound:peekinboundbytes:filteroutbound:peekoutboundbytes:))*