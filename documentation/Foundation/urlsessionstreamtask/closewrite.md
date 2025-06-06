# closeWrite()

**Framework**: Foundation  
**Kind**: method

Completes any enqueued reads and writes, and then closes the write side of the underlying socket.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func closeWrite()
```

#### Discussion

You may continue to read data using the [`readData(ofMinLength:maxLength:timeout:completionHandler:)`](urlsessionstreamtask/readdata(ofminlength:maxlength:timeout:completionhandler:).md) method after calling this method. Any calls to [`write(_:timeout:completionHandler:)`](urlsessionstreamtask/write(_:timeout:completionhandler:).md) after calling this method will result in an error.

Because the server may continue to write bytes to the client, it is recommended that you continue reading until the stream reaches end-of-file (EOF).

## See Also

- [func closeRead()](urlsessionstreamtask/closeread.md)
  Completes any enqueued reads and writes, and then closes the read side of the underlying socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/closewrite())*