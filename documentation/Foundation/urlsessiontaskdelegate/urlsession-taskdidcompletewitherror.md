# urlSession(_:task:didCompleteWithError:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the task finished transferring data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didCompleteWithError error: (any Error)?)
```

## Mentions

- [Pausing and resuming downloads](pausing-and-resuming-downloads.md)
- [Downloading files from websites](downloading-files-from-websites.md)
- [Fetching website data into memory](fetching-website-data-into-memory.md)
- [Pausing and resuming uploads](pausing-and-resuming-uploads.md)

#### Discussion

The only errors your delegate receives through the `error` parameter are client-side errors, such as being unable to resolve the hostname or connect to the host. To check for server-side errors, inspect the [`response`](urlsessiontask/response.md) property of the `task` parameter received by this callback.

## Parameters

- `session`: The session containing the task that has finished transferring data.
- `task`: The task that has finished transferring data.
- `error`: If an error occurred, an error object indicating how the transfer failed, otherwise  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didcompletewitherror:))*