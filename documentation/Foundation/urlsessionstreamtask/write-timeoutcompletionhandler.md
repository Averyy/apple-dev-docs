# write(_:timeout:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Asynchronously writes the specified data to the stream, and calls a handler upon completion.

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
func write(_ data: Data, timeout: TimeInterval) async throws
```

#### Discussion

There is no guarantee that the remote side of the stream has received all of the written bytes at the time that `completionHandler` is called, only that all of the data has been written to the kernel.

## Parameters

- `data`: The data to be written.
- `timeout`: A timeout for writing bytes. If the write is not completed within the specified interval, the write is canceled and the   is called with an error. Pass   to prevent a write from timing out.
- `completionHandler`: This completion handler takes the following parameter:

## See Also

- [func readData(ofMinLength: Int, maxLength: Int, timeout: TimeInterval, completionHandler: (Data?, Bool, (any Error)?) -> Void)](urlsessionstreamtask/readdata(ofminlength:maxlength:timeout:completionhandler:).md)
  Asynchronously reads a number of bytes from the stream, and calls a handler upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/write(_:timeout:completionhandler:))*