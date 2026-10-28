# maximumDatagramLength

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The maximum size of a datagram to be written currently.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_get_maximum_datagram_size(_:)`](../../Network/nw_connection_get_maximum_datagram_size%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var maximumDatagramLength: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger maximumDatagramLength;
```

## Discussion

If a datagram is written with a longer length than `maximumDatagramLength`, the datagram may be fragmented or encounter an error. Note that this value is not guaranteed to be the maximum datagram length for end-to-end communication across the network. Use Key-Value Observing to watch this property.

## See Also

### Transferring data
- [func setReadHandler(([Data]?, (any Error)?) -> Void, maxDatagrams: Int)](./setreadhandler%28_,maxdatagrams%29.md)
  Set a read handler for datagrams.
- [func writeDatagram(Data, completionHandler: ((any Error)?) -> Void)](./writedatagram%28_,completionhandler%29.md)
  Write a single datagram.
- [func writeMultipleDatagrams([Data], completionHandler: ((any Error)?) -> Void)](./writemultipledatagrams%28_,completionhandler%29.md)
  Write multiple datagrams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/maximumdatagramlength)*