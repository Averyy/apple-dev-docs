# writeClose()

**Framework**: Network Extension  
**Kind**: method

Close the connection for writing.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func writeClose()
```

#### Discussion

Close this connection’s write side such that further write requests won’t succeed. Note that this has the effect of closing the read side of the peer connection. When the connection’s read side and write side are closed, the connection is considered disconnected and will transition to the appropriate state.

## See Also

- [func readMinimumLength(Int, maximumLength: Int, completionHandler: (Data?, (any Error)?) -> Void)](nwtcpconnection/readminimumlength(_:maximumlength:completionhandler:).md)
  Read the requested range of bytes.
- [func readLength(Int, completionHandler: (Data?, (any Error)?) -> Void)](nwtcpconnection/readlength(_:completionhandler:).md)
  Read a certain number of bytes on a connection.
- [func write(Data, completionHandler: ((any Error)?) -> Void)](nwtcpconnection/write(_:completionhandler:).md)
  Write the data to the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/writeclose())*