# setReadHandler(_:maxDatagrams:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Set a read handler for datagrams.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_receive(_:_:_:_:)`](../../Network/nw_connection_receive%28_,_,_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
func setReadHandler(_ handler: @escaping ([Data]?, (any Error)?) -> Void, maxDatagrams: Int)
```

```objc
- (void) setReadHandler:(void (^)(NSArray<NSData *> *datagrams, NSError *error)) handler maxDatagrams:(NSUInteger) maxDatagrams;
```

## Discussion

Reads will be scheduled by the system, so this method only needs to be called once for a session.

## Parameters

- `handler`: A handler called when datagrams have been read, or when an error has occurred.
- `maxDatagrams`: The maximum number of datagrams to send to the handler.

## See Also

### Transferring data
- [func writeDatagram(Data, completionHandler: ((any Error)?) -> Void)](./writedatagram%28_,completionhandler%29.md)
  Write a single datagram.
- [func writeMultipleDatagrams([Data], completionHandler: ((any Error)?) -> Void)](./writemultipledatagrams%28_,completionhandler%29.md)
  Write multiple datagrams.
- [var maximumDatagramLength: Int](./maximumdatagramlength.md)
  The maximum size of a datagram to be written currently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/setreadhandler(_:maxdatagrams:))*