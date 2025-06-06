# NEFilterAction

**Framework**: Network Extension  
**Kind**: enum

The actions a data provider can take on a filter flow.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum NEFilterAction
```

#### Overview

The control provider receives a filter report when the data provider issues a verdict with the [`shouldReport`](nefilterverdict/shouldreport.md) property set to [`true`](https://developer.apple.com/documentation/swift/true). The report contains an [`action`](nefilterreport/action.md) property set to one of the values listed here.

## Topics

### Enumeration Cases
- [NEFilterAction.invalid](nefilteraction/invalid.md)
  Invalid action used to represent an error.
- [NEFilterAction.allow](nefilteraction/allow.md)
  Allow the flow.
- [NEFilterAction.drop](nefilteraction/drop.md)
  Drop the flow.
- [NEFilterAction.remediate](nefilteraction/remediate.md)
  Remediate the flow.
- [NEFilterAction.filterData](nefilteraction/filterdata.md)
  Filter data on the flow.
### Initializers
- [init?(rawValue: Int)](nefilteraction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var flow: NEFilterFlow?](nefilterreport/flow.md)
  The flow on which the associated action was taken.
- [var action: NEFilterAction](nefilterreport/action.md)
  The action taken on the reported flow.
- [var event: NEFilterReport.Event](nefilterreport/event-swift.property.md)
  The type of event indicated by this report.
- [NEFilterReport.Event](nefilterreport/event-swift.enum.md)
  A type that represents the kind of event indicated by a report.
- [var bytesInboundCount: Int](nefilterreport/bytesinboundcount.md)
  The number of inbound bytes received from the flow.
- [var bytesOutboundCount: Int](nefilterreport/bytesoutboundcount.md)
  The number of outbound bytes sent on the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilteraction)*