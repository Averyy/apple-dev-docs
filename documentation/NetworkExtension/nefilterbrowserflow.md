# NEFilterBrowserFlow

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A flow of network data, originating from a WebKit-based browser, that the filter examines.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class NEFilterBrowserFlow
```

```objc
@interface NEFilterBrowserFlow : NEFilterFlow
```

## Topics

### Getting browser flow properties
- [var parentURL: URL?](./nefilterbrowserflow/parenturl.md)
  A URL of the web page that’s responsible for the flow’s creation.
- [var request: URLRequest?](./nefilterbrowserflow/request.md)
  An HTTP request of the flow.
- [var response: URLResponse?](./nefilterbrowserflow/response.md)
  An HTTP response of the flow.

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
- [class NEFilterSocketFlow](./nefiltersocketflow.md)
  A flow of network data that the filter examines.
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

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow)*