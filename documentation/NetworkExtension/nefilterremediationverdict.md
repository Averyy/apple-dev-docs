# NEFilterRemediationVerdict

**Framework**: Network Extension  
**Kind**: class

The result from a filter data provider after the user requests remediation for a blocked flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class NEFilterRemediationVerdict
```

## Topics

### Creating remediation verdicts
- [class func allow() -> NEFilterRemediationVerdict](nefilterremediationverdict/allow.md)
  Create a verdict that indicates to the system that the Filter Data Provider will allow the flow to pass to its final destination when/if the flow is requested again.
- [class func drop() -> NEFilterRemediationVerdict](nefilterremediationverdict/drop.md)
  Create a verdict that indicates to the system that the Filter Data Provider will continue to block the flow of network data if/when the flow is requested again.
- [class func needRules() -> NEFilterRemediationVerdict](nefilterremediationverdict/needrules.md)
  Create a verdict that indicates to the system that the Filter Data Provider needs the filtering rules to be updated before it can make a remediation decision about the current flow of network data.

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
- [class NEFilterDataVerdict](nefilterdataverdict.md)
  The result from a filter data provder for subsequent chunks of data on a flow.
- [class NEFilterControlVerdict](nefiltercontrolverdict.md)
  The result from a filter control provider.
- [class NEFilterVerdict](nefilterverdict.md)
  The abstract base class for filter verdict classes.
- [class NEFilterReport](nefilterreport.md)
  The report of the data provider’s action on a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict)*