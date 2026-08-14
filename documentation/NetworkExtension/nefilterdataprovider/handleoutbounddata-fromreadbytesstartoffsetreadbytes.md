# handleOutboundData(from:readBytesStartOffset:readBytes:)

**Framework**: Network Extension  
**Kind**: method

Make a filtering decision about a chunk of outbound data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func handleOutboundData(from flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes: Data) -> NEFilterDataVerdict
```

#### Return Value

An [`NEFilterDataVerdict`](nefilterdataverdict.md) indicating how the system should handle the chunk of data and all subsequent outbound data for the flow.

#### Discussion

`NEFilterDataProvider` subclasses must override this method.

## Parameters

- `flow`: An [`NEFilterFlow`](nefilterflow.md) object containing information about the flow.
- `offset`: An unsigned integer containing the offset of the data stored in `readBytes`. This offset is measured from the beginning of the flow’s outbound data.
- `readBytes`: An [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) object containing the data to be filtered.

## See Also

- [func handleNewFlow(NEFilterFlow) -> NEFilterNewFlowVerdict](nefilterdataprovider/handlenewflow(_:).md)
  Make a filtering decision for a newly-created flow of network content.
- [func handleInboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddata(from:readbytesstartoffset:readbytes:).md)
  Make a filtering decision about a chunk of inbound data.
- [enum NEFilterDataAttribute](nefilterdataattribute.md)
  Attribute flags that describe the data handled by a filter.
- [func handleInboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the inbound data for a flow.
- [func handleOutboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleoutbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the outbound data for a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/handleoutbounddata(from:readbytesstartoffset:readbytes:))*