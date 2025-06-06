# NEFilterDataVerdict

**Framework**: Network Extension  
**Kind**: class

The result from a filter data provder for subsequent chunks of data on a flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEFilterDataVerdict
```

#### Overview

Return this verdict type from the various methods of [`NEFilterDataProvider`](nefilterdataprovider.md).

## Topics

### Creating data verdicts
- [class func allow() -> NEFilterDataVerdict](nefilterdataverdict/allow.md)
  Creates a verdict that tells the system to pass the current chunk of network data and all subsequent data for the current flow to its final destination.
- [class func drop() -> NEFilterDataVerdict](nefilterdataverdict/drop.md)
  Creates a verdict that tells the system to drop the current chunk of network data and all subsequent data for the current flow.
- [class func pause() -> NEFilterDataVerdict](nefilterdataverdict/pause.md)
  Creates a verdict that tells the system to pause the flow.
- [class func remediateVerdict(withRemediationURLMapKey: String?, remediationButtonTextMapKey: String?) -> NEFilterDataVerdict](nefilterdataverdict/remediateverdict(withremediationurlmapkey:remediationbuttontextmapkey:).md)
  Creates a verdict to drop the current chunk of network data and all subsequent data for the current flow, and provides a remediation URL.
- [class func needRules() -> NEFilterDataVerdict](nefilterdataverdict/needrules.md)
  Creates a verdict that tells the system that the Filter Control Provider needs to update the rules before making a decision about the flow’s data.
- [init(passBytes: Int, peekBytes: Int)](nefilterdataverdict/init(passbytes:peekbytes:).md)
  Creates a verdict that tells the system to pass a chunk of network data to its final destination, and specifies the next chunk of data to provide.
### Reporting statistics
- [var statisticsReportFrequency: NEFilterReport.Frequency](nefilterdataverdict/statisticsreportfrequency.md)
  The frequencty at which to provide flow statistics to the data provider.

## Relationships

### Inherits From
- [NEFilterVerdict](nefilterverdict.md)
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
- [class NEFilterNewFlowVerdict](nefilternewflowverdict.md)
  The result from a filter data provder after the initial examination of a flow.
- [class NEFilterControlVerdict](nefiltercontrolverdict.md)
  The result from a filter control provider.
- [class NEFilterRemediationVerdict](nefilterremediationverdict.md)
  The result from a filter data provider after the user requests remediation for a blocked flow.
- [class NEFilterVerdict](nefilterverdict.md)
  The abstract base class for filter verdict classes.
- [class NEFilterReport](nefilterreport.md)
  The report of the data provider’s action on a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataverdict)*