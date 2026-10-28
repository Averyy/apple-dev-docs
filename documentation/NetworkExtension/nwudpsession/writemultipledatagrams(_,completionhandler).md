# writeMultipleDatagrams(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Write multiple datagrams.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_send(_:_:_:_:_:)`](../../Network/nw_connection_send%28_,_,_,_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
func writeMultipleDatagrams(_ datagramArray: [Data], completionHandler: @escaping ((any Error)?) -> Void)
```

```objc
- (void) writeMultipleDatagrams:(NSArray<NSData *> *) datagramArray completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

Callers should wait until the `completionHandler` is executed before issuing another write.

## Parameters

- `datagramArray`: An [`NSArray`](../../Foundation/nsarray.md) of [`NSData`](../../Foundation/nsdata.md) objects, containing the ordered list of datagrams to write.
- `completionHandler`: A handler called when the write request has either succeeded or failed.

## See Also

### Transferring data
- [func setReadHandler(([Data]?, (any Error)?) -> Void, maxDatagrams: Int)](./setreadhandler%28_,maxdatagrams%29.md)
  Set a read handler for datagrams.
- [func writeDatagram(Data, completionHandler: ((any Error)?) -> Void)](./writedatagram%28_,completionhandler%29.md)
  Write a single datagram.
- [var maximumDatagramLength: Int](./maximumdatagramlength.md)
  The maximum size of a datagram to be written currently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/writemultipledatagrams(_:completionhandler:))*