# NEFilterReport.Event

**Framework**: Network Extension  
**Kind**: enum

A type that represents the kind of event indicated by a report.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum Event
```

## Topics

### Event Types
- [NEFilterReport.Event.newFlow](nefilterreport/event-swift.enum/newflow.md)
  A type of event indicating the report is for a new flow.
- [NEFilterReport.Event.dataDecision](nefilterreport/event-swift.enum/datadecision.md)
  A type of event indicating the report is about a pass/block decision made after analyzing some amount of a flow’s data.
- [NEFilterReport.Event.flowClosed](nefilterreport/event-swift.enum/flowclosed.md)
  A type of event indicating the report is for a flow’s closing.
- [NEFilterReport.Event.statistics](nefilterreport/event-swift.enum/statistics.md)
  A type of event indicating the report is for the latest statistics of the flow.
### Initializers
- [init?(rawValue: Int)](nefilterreport/event-swift.enum/init(rawvalue:).md)

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
- [enum NEFilterAction](nefilteraction.md)
  The actions a data provider can take on a filter flow.
- [var event: NEFilterReport.Event](nefilterreport/event-swift.property.md)
  The type of event indicated by this report.
- [var bytesInboundCount: Int](nefilterreport/bytesinboundcount.md)
  The number of inbound bytes received from the flow.
- [var bytesOutboundCount: Int](nefilterreport/bytesoutboundcount.md)
  The number of outbound bytes sent on the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterreport/event-swift.enum)*