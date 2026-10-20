# NEFilterControlVerdict

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The result from a filter control provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class NEFilterControlVerdict
```

```objc
@interface NEFilterControlVerdict : NEFilterNewFlowVerdict
```

## Topics

### Creating control verdicts
- [class func allow(withUpdateRules: Bool) -> NEFilterControlVerdict](./nefiltercontrolverdict/allow%28withupdaterules%29.md)
  Create a verdict that indicates to the system that all of the flow’s data should be allowed to pass to its final destination, and that the filtering rules have been updated.
- [class func drop(withUpdateRules: Bool) -> NEFilterControlVerdict](./nefiltercontrolverdict/drop%28withupdaterules%29.md)
  Create a verdict that indicates to the system that all of the flow’s data should be dropped, and that the filtering rules have been updated.
- [class func updateRules() -> NEFilterControlVerdict](./nefiltercontrolverdict/updaterules%28%29.md)
  Create a verdict that indicates to the system that the filtering rules have been updated, and that the Filter Data Provider needs to make a decision about the flow’s data.

## Relationships

### Inherits From
- [NEFilterNewFlowVerdict](./nefilternewflowverdict.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Flow handling
- [class NEFilterFlow](./nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [class NEFilterBrowserFlow](./nefilterbrowserflow.md)
  A flow of network data, originating from a WebKit-based browser, that the filter examines.
- [class NEFilterSocketFlow](./nefiltersocketflow.md)
  A flow of network data that the filter examines.
- [class NEFilterNewFlowVerdict](./nefilternewflowverdict.md)
  The result from a filter data provder after the initial examination of a flow.
- [class NEFilterDataVerdict](./nefilterdataverdict.md)
  The result from a filter data provder for subsequent chunks of data on a flow.
- [class NEFilterRemediationVerdict](./nefilterremediationverdict.md)
  The result from a filter data provider after the user requests remediation for a blocked flow.
- [class NEFilterVerdict](./nefilterverdict.md)
  The abstract base class for filter verdict classes.
- [class NEFilterReport](./nefilterreport.md)
  The report of the data provider’s action on a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict)*