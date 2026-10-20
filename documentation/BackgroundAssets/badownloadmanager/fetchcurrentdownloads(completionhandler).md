# fetchCurrentDownloads(completionHandler:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

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
func fetchCurrentDownloads(completionHandler: @escaping @Sendable ([BADownload], (any Error)?) -> Void)
```

```swift
var currentDownloads: [BADownload] { get async throws }
```

```objc
- (void) fetchCurrentDownloadsWithCompletionHandler:(void (^)(NSArray<BADownload *> *downloads, NSError *error)) completionHandler;
```

#### Discussion

The completion handler takes the following parameters:

- An array of scheduled and in-progress downloads.
- An error if a problems occurs, or `nil` if the method successfully fetches the current downloads.

## Parameters

- `completionHandler`: The handler that processes the fetch results, which the system executes on an arbitrary queue.

## See Also

### Fetching in-progress downloads
- [func fetchCurrentDownloads() throws -> [BADownload]](./fetchcurrentdownloads%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/fetchcurrentdownloads(completionhandler:))*