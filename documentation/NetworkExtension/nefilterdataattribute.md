# NEFilterDataAttribute

**Framework**: Network Extension  
**Kind**: enum

Attribute flags that describe the data handled by a filter.

**Availability**:
- macOS 10.15.5+

## Declaration

```swift
enum NEFilterDataAttribute
```

## Topics

### Attributes
- [NEFilterDataAttribute.hasIPHeader](nefilterdataattribute/hasipheader.md)
  An attribute that indicates the data includes an IP header.
### Initializers
- [init?(rawValue: Int)](nefilterdataattribute/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func handleNewFlow(NEFilterFlow) -> NEFilterNewFlowVerdict](nefilterdataprovider/handlenewflow(_:).md)
  Make a filtering decision for a newly-created flow of network content.
- [func handleInboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddata(from:readbytesstartoffset:readbytes:).md)
  Make a filtering decision about a chunk of inbound data.
- [func handleOutboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](nefilterdataprovider/handleoutbounddata(from:readbytesstartoffset:readbytes:).md)
  Make a filtering decision about a chunk of outbound data.
- [func handleInboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the inbound data for a flow.
- [func handleOutboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleoutbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the outbound data for a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataattribute)*