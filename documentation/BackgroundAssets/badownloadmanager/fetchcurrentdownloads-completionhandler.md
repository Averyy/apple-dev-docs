# fetchCurrentDownloads(completionHandler:)

**Framework**: Background Assets  
**Kind**: method

Fetches the contents of the manager’s download queue.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
var currentDownloads: [BADownload] { get async throws }
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as this page explains, or you can call it as an asynchronous method that has the following declaration: ```swift
var currentDownloads: [BADownload] { get async throws }
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The completion handler takes the following parameters:

- An array of scheduled and in-progress downloads.
- An error if a problems occurs, or `nil` if the method successfully fetches the current downloads.

## Parameters

- `completionHandler`: The handler that processes the fetch results, which the system executes on an arbitrary queue.

## See Also

- [func fetchCurrentDownloads() throws -> [BADownload]](badownloadmanager/fetchcurrentdownloads.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/fetchcurrentdownloads(completionhandler:))*