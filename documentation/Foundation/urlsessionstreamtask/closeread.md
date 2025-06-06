# closeRead()

**Framework**: Foundation  
**Kind**: method

Completes any enqueued reads and writes, and then closes the read side of the underlying socket.

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
func closeRead()
```

#### Discussion

You may continue to write data using the [`write(_:timeout:completionHandler:)`](urlsessionstreamtask/write(_:timeout:completionhandler:).md) method after calling this method. Any calls to [`readData(ofMinLength:maxLength:timeout:completionHandler:)`](urlsessionstreamtask/readdata(ofminlength:maxlength:timeout:completionhandler:).md) after calling this method will result in an error.

## See Also

- [func closeWrite()](urlsessionstreamtask/closewrite.md)
  Completes any enqueued reads and writes, and then closes the write side of the underlying socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/closeread())*