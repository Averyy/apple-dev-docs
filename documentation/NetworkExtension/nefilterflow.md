# NEFilterFlow

**Framework**: Network Extension  
**Kind**: class

The abstract base class for types that represent flows of network data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEFilterFlow
```

## Topics

### Inspecting flow properties
- [var url: URL?](nefilterflow/url.md)
  The flow’s HTTP URL.
- [var identifier: UUID](nefilterflow/identifier.md)
  The unique identifier of the flow.
- [var direction: NETrafficDirection](nefilterflow/direction.md)
  The initial direction of the flow: incoming or outgoing.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.
- [var NEFilterFlowBytesMax: UInt64](nefilterflowbytesmax.md)
  The maximum number of bytes to pass or peek for a flow.
### Source app identification
- [var sourceAppUniqueIdentifier: Data?](nefilterflow/sourceappuniqueidentifier.md)
  A byte string that uniquely identifies the binary for each build of the app that is the source of the flow.
- [var sourceAppIdentifier: String?](nefilterflow/sourceappidentifier.md)
  A string containing the identifier of the source app of the flow.
- [var sourceAppVersion: String?](nefilterflow/sourceappversion.md)
  The short version string of the app that is the source of the flow.
- [var sourceAppAuditToken: Data?](nefilterflow/sourceappaudittoken.md)
  The audit token of the source application of the flow.
- [var sourceProcessAuditToken: Data?](nefilterflow/sourceprocessaudittoken.md)
  The audit token of the process that created the flow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NEFilterBrowserFlow](nefilterbrowserflow.md)
- [NEFilterSocketFlow](nefiltersocketflow.md)
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
- [class NEFilterReport](nefilterreport.md)
  The report of the data provider’s action on a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow)*