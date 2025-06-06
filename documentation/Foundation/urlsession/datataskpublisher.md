# URLSession.DataTaskPublisher

**Framework**: Foundation  
**Kind**: struct

A publisher that delivers the results of performing URL session data tasks.

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
struct DataTaskPublisher
```

## Mentions

- [Processing URL session data task results with Combine](processing-url-session-data-task-results-with-combine.md)

## Topics

### Creating a data task publisher
- [init(request: URLRequest, session: URLSession)](urlsession/datataskpublisher/init(request:session:).md)
  Creates a data task publisher from the provided URL request and URL session.
### Inspecting data task properties
- [let request: URLRequest](urlsession/datataskpublisher/request.md)
  The URL request performed by the data task associated with this publisher.
- [let session: URLSession](urlsession/datataskpublisher/session.md)
  The URL session that performs the data task associated with this publisher.

## Relationships

### Conforms To
- [Publisher](../Combine/Publisher.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Processing URL session data task results with Combine](processing-url-session-data-task-results-with-combine.md)
  Use a chain of asynchronous operators to receive and process data fetched from a URL.
- [func dataTaskPublisher(for: URLRequest) -> URLSession.DataTaskPublisher](urlsession/datataskpublisher(for:)-61v3e.md)
  Returns a publisher that wraps a URL session data task for a given URL request.
- [func dataTaskPublisher(for: URL) -> URLSession.DataTaskPublisher](urlsession/datataskpublisher(for:)-5kiir.md)
  Returns a publisher that wraps a URL session data task for a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/datataskpublisher)*