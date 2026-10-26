# NEFilterSocketFlow

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A flow of network data that the filter examines.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEFilterSocketFlow
```

```objc
@interface NEFilterSocketFlow : NEFilterFlow
```

## Topics

### Getting socket flow properties
- [var remoteEndpoint: NWEndpoint?](./nefiltersocketflow/remoteendpoint.md)
  An object containing details about the socket’s remote endpoint.
- [var remoteHostname: String?](./nefiltersocketflow/remotehostname.md)
  The flow’s remote hostname, if applicable.
- [class NEFilterFlow](./nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [var localEndpoint: NWEndpoint?](./nefiltersocketflow/localendpoint.md)
  An object containing details about the socket’s local endpoint.
- [var socketFamily: Int32](./nefiltersocketflow/socketfamily.md)
  The protocol family of the socket.
- [var socketType: Int32](./nefiltersocketflow/sockettype.md)
  The type of the socket.
- [var socketProtocol: Int32](./nefiltersocketflow/socketprotocol.md)
  The protocol of the socket.
### Instance Properties
- [var localFlowEndpoint: NWEndpoint?](./nefiltersocketflow/localflowendpoint-89z3l.md)
- [var remoteFlowEndpoint: NWEndpoint?](./nefiltersocketflow/remoteflowendpoint-6bnas.md)
- [localFlowEndpoint](./nefiltersocketflow/localflowendpoint-4nt54.md)
- [remoteFlowEndpoint](./nefiltersocketflow/remoteflowendpoint-52dxr.md)

## Relationships

### Inherits From
- [NEFilterFlow](./nefilterflow.md)
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
- [class NEFilterNewFlowVerdict](./nefilternewflowverdict.md)
  The result from a filter data provder after the initial examination of a flow.
- [class NEFilterDataVerdict](./nefilterdataverdict.md)
  The result from a filter data provder for subsequent chunks of data on a flow.
- [class NEFilterControlVerdict](./nefiltercontrolverdict.md)
  The result from a filter control provider.
- [class NEFilterRemediationVerdict](./nefilterremediationverdict.md)
  The result from a filter data provider after the user requests remediation for a blocked flow.
- [class NEFilterVerdict](./nefilterverdict.md)
  The abstract base class for filter verdict classes.
- [class NEFilterReport](./nefilterreport.md)
  The report of the data provider’s action on a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersocketflow)*