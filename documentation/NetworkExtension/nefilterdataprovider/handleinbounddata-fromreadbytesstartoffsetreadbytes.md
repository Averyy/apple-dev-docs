# handleInboundData(from:readBytesStartOffset:readBytes:)

**Framework**: Network Extension  
**Kind**: method

Make a filtering decision about a chunk of inbound data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func handleInboundData(from flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes: Data) -> NEFilterDataVerdict
```

#### Return Value

A [`NEFilterDataVerdict`](nefilterdataverdict.md) object indicating how the system should handle the chunk of data and all subsequent inbound data for the flow.

#### Discussion

`NEFilterDataProvider` subclasses must override this method.

## Parameters

- `flow`: An [`NEFilterFlow`](nefilterflow.md) object containing information about the flow.
- `offset`: An unsigned integer containing the offset of the data stored in `readBytes`. This offset is measured from the beginning of the flow’s inbound data.
- `readBytes`: An [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) object containing the data to filter. For non-UDP/TCP flows, since the data may optionally include the IP header, `readBytes` includes a 4-byte [`NEFilterDataAttribute`](nefilterdataattribute.md) field preceding the user data. Your handler must examine the [`NEFilterDataAttribute`](nefilterdataattribute.md) field and handle the data accordingly.

## See Also

- [func handleNewFlow(NEFilterFlow) -> NEFilterNewFlowVerdict](nefilterdataprovider/handlenewflow(_:).md)
  Make a filtering decision for a newly-created flow of network content.
- [enum NEFilterDataAttribute](nefilterdataattribute.md)
  Attribute flags that describe the data handled by a filter.
- [func handleOutboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](nefilterdataprovider/handleoutbounddata(from:readbytesstartoffset:readbytes:).md)
  Make a filtering decision about a chunk of outbound data.
- [func handleInboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the inbound data for a flow.
- [func handleOutboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleoutbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the outbound data for a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/handleinbounddata(from:readbytesstartoffset:readbytes:))*