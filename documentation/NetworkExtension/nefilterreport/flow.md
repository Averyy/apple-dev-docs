# flow

**Framework**: Network Extension  
**Kind**: property

The flow on which the associated action was taken.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var flow: NEFilterFlow? { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterreport/flow)*