# write(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Write the data to the connection.

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
func write(_ data: Data, completionHandler completion: @escaping ((any Error)?) -> Void)
```

```objc
- (void) write:(NSData *) data completionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

Callers should wait until the `completionHandler` is executed before issuing another write.

## Parameters

- `data`: The data object whose content will be written.
- `completion`: The completion handler to be invoked when the data content has been written or an error has occurred. If `error` is `nil`, the write succeeded and the caller can write more data.

## See Also

### Transferring data
- [func readMinimumLength(Int, maximumLength: Int, completionHandler: (Data?, (any Error)?) -> Void)](./readminimumlength%28_,maximumlength,completionhandler%29.md)
  Read the requested range of bytes.
- [func readLength(Int, completionHandler: (Data?, (any Error)?) -> Void)](./readlength%28_,completionhandler%29.md)
  Read a certain number of bytes on a connection.
- [func writeClose()](./writeclose%28%29.md)
  Close the connection for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/write(_:completionhandler:))*