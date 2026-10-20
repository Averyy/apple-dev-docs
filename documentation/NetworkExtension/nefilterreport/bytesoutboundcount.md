# bytesOutboundCount

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The number of outbound bytes sent on the flow.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var bytesOutboundCount: Int { get }
```

```objc
@property (readonly) NSUInteger bytesOutboundCount;
```

#### Discussion

This property is only non-zero when the report [`event`](./event-swift.property.md) is [`NEFilterReport.Event.flowClosed`](./event-swift.enum/flowclosed.md).

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
- [NEFilterReport.Event](./event-swift.enum.md)
  A type that represents the kind of event indicated by a report.
- [var bytesInboundCount: Int](./bytesinboundcount.md)
  The number of inbound bytes received from the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterreport/bytesoutboundcount)*