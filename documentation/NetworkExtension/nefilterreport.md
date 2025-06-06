# NEFilterReport

**Framework**: Network Extension  
**Kind**: class

The report of the data provider’s action on a flow.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEFilterReport
```

#### Overview

The system issues a report by calling your control provider’s [`handle(_:)`](nefilterprovider/handle(_:).md) method with a report instance when the data provider issues a verdict whose [`shouldReport`](nefilterverdict/shouldreport.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true).

## Topics

### Getting report properties
- [var flow: NEFilterFlow?](nefilterreport/flow.md)
  The flow on which the associated action was taken.
- [var action: NEFilterAction](nefilterreport/action.md)
  The action taken on the reported flow.
- [enum NEFilterAction](nefilteraction.md)
  The actions a data provider can take on a filter flow.
- [var event: NEFilterReport.Event](nefilterreport/event-swift.property.md)
  The type of event indicated by this report.
- [NEFilterReport.Event](nefilterreport/event-swift.enum.md)
  A type that represents the kind of event indicated by a report.
- [var bytesInboundCount: Int](nefilterreport/bytesinboundcount.md)
  The number of inbound bytes received from the flow.
- [var bytesOutboundCount: Int](nefilterreport/bytesoutboundcount.md)
  The number of outbound bytes sent on the flow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class NEFilterRemediationVerdict](nefilterremediationverdict.md)
  The result from a filter data provider after the user requests remediation for a blocked flow.
- [class NEFilterVerdict](nefilterverdict.md)
  The abstract base class for filter verdict classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterreport)*