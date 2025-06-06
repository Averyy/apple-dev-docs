# handleOutboundDataComplete(for:)

**Framework**: Network Extension  
**Kind**: method

Make a filtering decision after seeing all of the outbound data for a flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func handleOutboundDataComplete(for flow: NEFilterFlow) -> NEFilterDataVerdict
```

#### Return Value

An [`NEFilterDataVerdict`](nefilterdataverdict.md) object indicating how the system should handle the flow of network content.

#### Discussion

The system calls this method after all of the outbound data for a flow of network content has been given to the Filter Data Provider.

`NEFilterDataProvider` subclasses must override this method.

## Parameters

- `flow`: An   object containing information about the flow.

## See Also

- [func handleNewFlow(NEFilterFlow) -> NEFilterNewFlowVerdict](nefilterdataprovider/handlenewflow(_:).md)
  Make a filtering decision for a newly-created flow of network content.
- [func handleInboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddata(from:readbytesstartoffset:readbytes:).md)
  Make a filtering decision about a chunk of inbound data.
- [enum NEFilterDataAttribute](nefilterdataattribute.md)
  Attribute flags that describe the data handled by a filter.
- [func handleOutboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](nefilterdataprovider/handleoutbounddata(from:readbytesstartoffset:readbytes:).md)
  Make a filtering decision about a chunk of outbound data.
- [func handleInboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the inbound data for a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/handleoutbounddatacomplete(for:))*