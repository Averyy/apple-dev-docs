# readMinimumLength(_:maximumLength:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Read the requested range of bytes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func readMinimumLength(_ minimum: Int, maximumLength maximum: Int, completionHandler completion: @escaping (Data?, (any Error)?) -> Void)
```

#### Discussion

The completion handler will be invoked when:

- The exact number of requested bytes have been read; `data` will be non-`nil`.
- Fewer than the requested number of bytes, or no bytes, have been read, and the connection’s read side has been closed. `data` might be `nil`, depending on whether there was any data to be read when the connection’s read side was closed.
- Some fatal error has occurred, returned in `error`, and `data` will be nil.

To know when to schedule a read again, check for the condition whether an error has occurred.

For better performance, the caller should pick the effective minimum and maximum lengths. For example, if the caller absolutely needs a specific number of bytes before it can make any progress, use that value as the minimum. The maximum bytes can be the upperbound  that the caller wants to read. Typically, the minimum length can be the caller protocol fixed-size header and the maximum length can be the maximum size of the payload or  the size of the current read buffer.

## Parameters

- `minimum`: The minimum number of bytes the caller wants to read.
- `maximum`: The maximum number of bytes the caller wants to read.
- `completion`: The completion handler to be invoked when data has been read or an error occurred.

## See Also

- [func readLength(Int, completionHandler: (Data?, (any Error)?) -> Void)](nwtcpconnection/readlength(_:completionhandler:).md)
  Read a certain number of bytes on a connection.
- [func write(Data, completionHandler: ((any Error)?) -> Void)](nwtcpconnection/write(_:completionhandler:).md)
  Write the data to the connection.
- [func writeClose()](nwtcpconnection/writeclose.md)
  Close the connection for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/readminimumlength(_:maximumlength:completionhandler:))*