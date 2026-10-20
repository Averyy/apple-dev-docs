# readLength(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Read a certain number of bytes on a connection.

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
func readLength(_ length: Int, completionHandler completion: @escaping (Data?, (any Error)?) -> Void)
```

```objc
- (void) readLength:(NSUInteger) length completionHandler:(void (^)(NSData *data, NSError *error)) completion;
```

#### Discussion

Read `length` number of bytes. See `readMinimumLength:maximumLength:completionHandler:` for a complete discussion of the callback behavior.

## Parameters

- `length`: The exact number of bytes the caller wants to read.
- `completion`: The completion handler to be invoked when data has been read or an error occurred.

## See Also

### Transferring data
- [func readMinimumLength(Int, maximumLength: Int, completionHandler: (Data?, (any Error)?) -> Void)](./readminimumlength%28_,maximumlength,completionhandler%29.md)
  Read the requested range of bytes.
- [func write(Data, completionHandler: ((any Error)?) -> Void)](./write%28_,completionhandler%29.md)
  Write the data to the connection.
- [func writeClose()](./writeclose%28%29.md)
  Close the connection for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/readlength(_:completionhandler:))*