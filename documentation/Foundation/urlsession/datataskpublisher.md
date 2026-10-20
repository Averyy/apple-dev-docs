# URLSession.DataTaskPublisher

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

- [Processing URL session data task results with Combine](../processing-url-session-data-task-results-with-combine.md)

## Topics

### Declaring publisher topography
- [URLSession.DataTaskPublisher.Output](./datataskpublisher/output.md)
  The kind of values published by this publisher.
- [URLSession.DataTaskPublisher.Failure](./datataskpublisher/failure.md)
  The kind of errors this publisher might publish.
### Creating a data task publisher
- [init(request: URLRequest, session: URLSession)](./datataskpublisher/init%28request,session%29.md)
  Creates a data task publisher from the provided URL request and URL session.
### Inspecting data task properties
- [let request: URLRequest](./datataskpublisher/request.md)
  The URL request performed by the data task associated with this publisher.
- [let session: URLSession](./datataskpublisher/session.md)
  The URL session that performs the data task associated with this publisher.

## Relationships

### Conforms To
- [Publisher](../../Combine/publisher.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing tasks as a Combine Publisher
- [Processing URL session data task results with Combine](../processing-url-session-data-task-results-with-combine.md)
  Use a chain of asynchronous operators to receive and process data fetched from a URL.
- [func dataTaskPublisher(for: URLRequest) -> URLSession.DataTaskPublisher](./datataskpublisher%28for%29-61v3e.md)
  Returns a publisher that wraps a URL session data task for a given URL request.
- [func dataTaskPublisher(for: URL) -> URLSession.DataTaskPublisher](./datataskpublisher%28for%29-5kiir.md)
  Returns a publisher that wraps a URL session data task for a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/datataskpublisher)*