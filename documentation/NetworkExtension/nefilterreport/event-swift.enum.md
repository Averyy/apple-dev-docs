# NEFilterReport.Event

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NEFilterReportEvent : NSInteger;
```

## Topics

### Event Types
- [NEFilterReport.Event.newFlow](./event-swift.enum/newflow.md)
  A type of event indicating the report is for a new flow.
- [NEFilterReport.Event.dataDecision](./event-swift.enum/datadecision.md)
  A type of event indicating the report is about a pass/block decision made after analyzing some amount of a flow’s data.
- [NEFilterReport.Event.flowClosed](./event-swift.enum/flowclosed.md)
  A type of event indicating the report is for a flow’s closing.
- [NEFilterReport.Event.statistics](./event-swift.enum/statistics.md)
  A type of event indicating the report is for the latest statistics of the flow.
### Initializers
- [init?(rawValue: Int)](./event-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting report properties
- [var flow: NEFilterFlow?](./flow.md)
  The flow on which the associated action was taken.
- [var action: NEFilterAction](./action.md)
  The action taken on the reported flow.
- [enum NEFilterAction](../nefilteraction.md)
  The actions a data provider can take on a filter flow.
- [var event: NEFilterReport.Event](./event-swift.property.md)
  The type of event indicated by this report.
- [var bytesInboundCount: Int](./bytesinboundcount.md)
  The number of inbound bytes received from the flow.
- [var bytesOutboundCount: Int](./bytesoutboundcount.md)
  The number of outbound bytes sent on the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterreport/event-swift.enum)*