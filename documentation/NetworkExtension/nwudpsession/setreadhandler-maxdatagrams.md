# setReadHandler(_:maxDatagrams:)

**Framework**: Network Extension  
**Kind**: method

Set a read handler for datagrams.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setReadHandler(_ handler: @escaping ([Data]?, (any Error)?) -> Void, maxDatagrams: Int)
```

#### Discussion

Reads will be scheduled by the system, so this method only needs to be called once for a session.

## Parameters

- `handler`: A handler called when datagrams have been read, or when an error has occurred.
- `maxDatagrams`: The maximum number of datagrams to send to the handler.

## See Also

- [func writeDatagram(Data, completionHandler: ((any Error)?) -> Void)](nwudpsession/writedatagram(_:completionhandler:).md)
  Write a single datagram.
- [func writeMultipleDatagrams([Data], completionHandler: ((any Error)?) -> Void)](nwudpsession/writemultipledatagrams(_:completionhandler:).md)
  Write multiple datagrams.
- [var maximumDatagramLength: Int](nwudpsession/maximumdatagramlength.md)
  The maximum size of a datagram to be written currently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/setreadhandler(_:maxdatagrams:))*