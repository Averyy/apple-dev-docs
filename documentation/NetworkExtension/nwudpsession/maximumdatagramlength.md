# maximumDatagramLength

**Framework**: Network Extension  
**Kind**: property

The maximum size of a datagram to be written currently.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var maximumDatagramLength: Int { get }
```

#### Discussion

If a datagram is written with a longer length than `maximumDatagramLength`, the datagram may be fragmented or encounter an error. Note that this value is not guaranteed to be the maximum datagram length for end-to-end communication across the network. Use Key-Value Observing to watch this property.

## See Also

- [func setReadHandler(([Data]?, (any Error)?) -> Void, maxDatagrams: Int)](nwudpsession/setreadhandler(_:maxdatagrams:).md)
  Set a read handler for datagrams.
- [func writeDatagram(Data, completionHandler: ((any Error)?) -> Void)](nwudpsession/writedatagram(_:completionhandler:).md)
  Write a single datagram.
- [func writeMultipleDatagrams([Data], completionHandler: ((any Error)?) -> Void)](nwudpsession/writemultipledatagrams(_:completionhandler:).md)
  Write multiple datagrams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/maximumdatagramlength)*