# readLength(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Read a certain number of bytes on a connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func readLength(_ length: Int, completionHandler completion: @escaping (Data?, (any Error)?) -> Void)
```

#### Discussion

Read `length` number of bytes. See `readMinimumLength:maximumLength:completionHandler:` for a complete discussion of the callback behavior.

## Parameters

- `length`: The exact number of bytes the caller wants to read.
- `completion`: The completion handler to be invoked when data has been read or an error occurred.

## See Also

- [func readMinimumLength(Int, maximumLength: Int, completionHandler: (Data?, (any Error)?) -> Void)](nwtcpconnection/readminimumlength(_:maximumlength:completionhandler:).md)
  Read the requested range of bytes.
- [func write(Data, completionHandler: ((any Error)?) -> Void)](nwtcpconnection/write(_:completionhandler:).md)
  Write the data to the connection.
- [func writeClose()](nwtcpconnection/writeclose.md)
  Close the connection for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/readlength(_:completionhandler:))*