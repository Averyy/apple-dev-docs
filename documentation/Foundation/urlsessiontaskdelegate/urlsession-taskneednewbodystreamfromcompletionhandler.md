# urlSession(_:task:needNewBodyStreamFrom:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate if a task requires a new body stream starting from the given offset. This may be necessary when resuming a failed upload task.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, needNewBodyStreamForTask task: URLSessionTask, from offset: Int64) async -> InputStream?
```

## Parameters

- `session`: The session containing the task that needs a new body stream from the given offset.
- `task`: The task that needs a new body stream.
- `offset`: The starting offset required for the body stream.
- `completionHandler`: A completion handler that your delegate method should call with the new body stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:neednewbodystreamfrom:completionhandler:))*