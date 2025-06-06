# NEFilterNewFlowVerdict

**Framework**: Network Extension  
**Kind**: class

The result from a filter data provder after the initial examination of a flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEFilterNewFlowVerdict
```

## Topics

### Creating new flow verdicts
- [class func allow() -> NEFilterNewFlowVerdict](nefilternewflowverdict/allow.md)
  Create a verdict that indicates to the system that the all of the new flow’s data should be allowed to pass to its final destination.
- [class func drop() -> NEFilterNewFlowVerdict](nefilternewflowverdict/drop.md)
  Create a verdict that indicates to the system that all of the new flow’s data should dropped, and the user should not be given the opportunity to request access.
- [class func pause() -> NEFilterNewFlowVerdict](nefilternewflowverdict/pause.md)
  Creates a verdict that tells the system to pause the flow.
- [class func filterDataVerdict(withFilterInbound: Bool, peekInboundBytes: Int, filterOutbound: Bool, peekOutboundBytes: Int) -> NEFilterNewFlowVerdict](nefilternewflowverdict/filterdataverdict(withfilterinbound:peekinboundbytes:filteroutbound:peekoutboundbytes:).md)
  Create a verdict that indicates to the system that the filter needs to make a decision about a new flow after seeing a portion of the flow’s data.
- [class func remediateVerdict(withRemediationURLMapKey: String, remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict](nefilternewflowverdict/remediateverdict(withremediationurlmapkey:remediationbuttontextmapkey:).md)
  Create a verdict that indicates to the system that all of the new flow’s data should be dropped, but allow the user to request access by tapping or clicking on a URL.
- [class func needRules() -> NEFilterNewFlowVerdict](nefilternewflowverdict/needrules.md)
  Create a verdict that indicates to the system that the Filter Data Provider needs more information before it can make a decision about a new flow.
- [class func urlAppendStringVerdict(withMapKey: String) -> NEFilterNewFlowVerdict](nefilternewflowverdict/urlappendstringverdict(withmapkey:).md)
  Create a verdict that indicates to the system that all of the new flow’s data should be allowed to pass to its final destination, but a string should first be appended to the new flow’s request URL.
### Inspecting new flow verdict properties
- [var statisticsReportFrequency: NEFilterReport.Frequency](nefilternewflowverdict/statisticsreportfrequency.md)
  The frequency at which the data provider receives reports.
- [NEFilterReport.Frequency](nefilterreport/frequency.md)
  An enumeration that represents the frequency of filter report delivery.

## Relationships

### Inherits From
- [NEFilterVerdict](nefilterverdict.md)
### Inherited By
- [NEFilterControlVerdict](nefiltercontrolverdict.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NEFilterFlow](nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [class NEFilterBrowserFlow](nefilterbrowserflow.md)
  A flow of network data, originating from a WebKit-based browser, that the filter examines.
- [class NEFilterSocketFlow](nefiltersocketflow.md)
  A flow of network data that the filter examines.
- [class NEFilterDataVerdict](nefilterdataverdict.md)
  The result from a filter data provder for subsequent chunks of data on a flow.
- [class NEFilterControlVerdict](nefiltercontrolverdict.md)
  The result from a filter control provider.
- [class NEFilterRemediationVerdict](nefilterremediationverdict.md)
  The result from a filter data provider after the user requests remediation for a blocked flow.
- [class NEFilterVerdict](nefilterverdict.md)
  The abstract base class for filter verdict classes.
- [class NEFilterReport](nefilterreport.md)
  The report of the data provider’s action on a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict)*