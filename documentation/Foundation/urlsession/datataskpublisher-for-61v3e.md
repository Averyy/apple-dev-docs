# dataTaskPublisher(for:)

**Framework**: Foundation  
**Kind**: method

Returns a publisher that wraps a URL session data task for a given URL request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func dataTaskPublisher(for request: URLRequest) -> URLSession.DataTaskPublisher
```

#### Discussion

The publisher publishes data when the task completes, or terminates if the task fails with an error.

## Parameters

- `request`: The URL request for which to create a data task.

## See Also

- [Processing URL session data task results with Combine](processing-url-session-data-task-results-with-combine.md)
  Use a chain of asynchronous operators to receive and process data fetched from a URL.
- [func dataTaskPublisher(for: URL) -> URLSession.DataTaskPublisher](urlsession/datataskpublisher(for:)-5kiir.md)
  Returns a publisher that wraps a URL session data task for a given URL.
- [URLSession.DataTaskPublisher](urlsession/datataskpublisher.md)
  A publisher that delivers the results of performing URL session data tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/datataskpublisher(for:)-61v3e)*