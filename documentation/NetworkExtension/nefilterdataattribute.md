# NEFilterDataAttribute

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

Attribute flags that describe the data handled by a filter.

**Availability**:
- macOS 10.15.5+

## Declaration

```swift
enum NEFilterDataAttribute
```

```c
enum NEFilterDataAttribute : NSInteger;
```

## Topics

### Attributes
- [NEFilterDataAttribute.hasIPHeader](./nefilterdataattribute/hasipheader.md)
  An attribute that indicates the data includes an IP header.
### Initializers
- [init?(rawValue: Int)](./nefilterdataattribute/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Filtering network content
- [func handleNewFlow(NEFilterFlow) -> NEFilterNewFlowVerdict](./nefilterdataprovider/handlenewflow%28_%29.md)
  Make a filtering decision for a newly-created flow of network content.
- [func handleInboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](./nefilterdataprovider/handleinbounddata%28from,readbytesstartoffset,readbytes%29.md)
  Make a filtering decision about a chunk of inbound data.
- [func handleOutboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](./nefilterdataprovider/handleoutbounddata%28from,readbytesstartoffset,readbytes%29.md)
  Make a filtering decision about a chunk of outbound data.
- [func handleInboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](./nefilterdataprovider/handleinbounddatacomplete%28for%29.md)
  Make a filtering decision after seeing all of the inbound data for a flow.
- [func handleOutboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](./nefilterdataprovider/handleoutbounddatacomplete%28for%29.md)
  Make a filtering decision after seeing all of the outbound data for a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataattribute)*