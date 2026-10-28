# writeClose()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Close the connection for writing.

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
func writeClose()
```

```objc
- (void) writeClose;
```

## Discussion

Close this connection’s write side such that further write requests won’t succeed. Note that this has the effect of closing the read side of the peer connection. When the connection’s read side and write side are closed, the connection is considered disconnected and will transition to the appropriate state.

## See Also

### Transferring data
- [func readMinimumLength(Int, maximumLength: Int, completionHandler: (Data?, (any Error)?) -> Void)](./readminimumlength%28_,maximumlength,completionhandler%29.md)
  Read the requested range of bytes.
- [func readLength(Int, completionHandler: (Data?, (any Error)?) -> Void)](./readlength%28_,completionhandler%29.md)
  Read a certain number of bytes on a connection.
- [func write(Data, completionHandler: ((any Error)?) -> Void)](./write%28_,completionhandler%29.md)
  Write the data to the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/writeclose())*