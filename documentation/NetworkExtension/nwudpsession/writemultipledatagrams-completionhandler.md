# writeMultipleDatagrams(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Write multiple datagrams.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func writeMultipleDatagrams(_ datagramArray: [Data], completionHandler: @escaping ((any Error)?) -> Void)
```

#### Discussion

Callers should wait until the `completionHandler` is executed before issuing another write.

## Parameters

- `datagramArray`: An   of   objects, containing the ordered list of datagrams to write.
- `completionHandler`: A handler called when the write request has either succeeded or failed.

## See Also

- [func setReadHandler(([Data]?, (any Error)?) -> Void, maxDatagrams: Int)](nwudpsession/setreadhandler(_:maxdatagrams:).md)
  Set a read handler for datagrams.
- [func writeDatagram(Data, completionHandler: ((any Error)?) -> Void)](nwudpsession/writedatagram(_:completionhandler:).md)
  Write a single datagram.
- [var maximumDatagramLength: Int](nwudpsession/maximumdatagramlength.md)
  The maximum size of a datagram to be written currently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/writemultipledatagrams(_:completionhandler:))*