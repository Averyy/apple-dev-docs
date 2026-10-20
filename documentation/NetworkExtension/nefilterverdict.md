# NEFilterVerdict

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The abstract base class for filter verdict classes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEFilterVerdict
```

```objc
@interface NEFilterVerdict : NSObject
```

#### Overview

Filter providers use instances this class to inform the system about how to handle flows of network data.

## Topics

### Configuring report generation
- [var shouldReport: Bool](./nefilterverdict/shouldreport.md)
  A Boolean value that indicates whether to send a report to the control provider when processing this verdict.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NEFilterDataVerdict](./nefilterdataverdict.md)
- [NEFilterNewFlowVerdict](./nefilternewflowverdict.md)
- [NEFilterRemediationVerdict](./nefilterremediationverdict.md)
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
- [class NEFilterControlVerdict](./nefiltercontrolverdict.md)
  The result from a filter control provider.
- [class NEFilterRemediationVerdict](./nefilterremediationverdict.md)
  The result from a filter data provider after the user requests remediation for a blocked flow.
- [class NEFilterReport](./nefilterreport.md)
  The report of the data provider’s action on a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterverdict)*