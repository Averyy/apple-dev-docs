# write(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Write the data to the connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func write(_ data: Data, completionHandler completion: @escaping ((any Error)?) -> Void)
```

#### Discussion

Callers should wait until the `completionHandler` is executed before issuing another write.

## Parameters

- `data`: The data object whose content will be written.
- `completion`: The completion handler to be invoked when the data content has been written or an error has occurred.   If   is  , the write succeeded and the caller can write more data.

## See Also

- [func readMinimumLength(Int, maximumLength: Int, completionHandler: (Data?, (any Error)?) -> Void)](nwtcpconnection/readminimumlength(_:maximumlength:completionhandler:).md)
  Read the requested range of bytes.
- [func readLength(Int, completionHandler: (Data?, (any Error)?) -> Void)](nwtcpconnection/readlength(_:completionhandler:).md)
  Read a certain number of bytes on a connection.
- [func writeClose()](nwtcpconnection/writeclose.md)
  Close the connection for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/write(_:completionhandler:))*