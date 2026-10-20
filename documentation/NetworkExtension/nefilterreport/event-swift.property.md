# event

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The type of event indicated by this report.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var event: NEFilterReport.Event { get }
```

```objc
@property (readonly) NEFilterReportEvent event;
```

## See Also

### Getting report properties
- [var flow: NEFilterFlow?](./flow.md)
  The flow on which the associated action was taken.
- [var action: NEFilterAction](./action.md)
  The action taken on the reported flow.
- [enum NEFilterAction](../nefilteraction.md)
  The actions a data provider can take on a filter flow.
- [NEFilterReport.Event](./event-swift.enum.md)
  A type that represents the kind of event indicated by a report.
- [var bytesInboundCount: Int](./bytesinboundcount.md)
  The number of inbound bytes received from the flow.
- [var bytesOutboundCount: Int](./bytesoutboundcount.md)
  The number of outbound bytes sent on the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterreport/event-swift.property)*