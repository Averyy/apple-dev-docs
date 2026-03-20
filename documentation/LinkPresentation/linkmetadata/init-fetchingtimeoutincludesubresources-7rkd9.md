# init(fetching:timeout:includeSubresources:)

**Framework**: Link Presentation  
**Kind**: init

Creates a [`LinkMetadata`](linkmetadata.md) value from the specified properties by fetching the URL using the specified request.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
nonisolated
init(fetching request: URLRequest, timeout: Duration = .seconds(30), includeSubresources: Bool = true) async throws
```

#### Discussion

Metadata fetching supports Task cancellation; if the enclosing Task is cancelled, the metadata request will be cancelled.

## Parameters

- `request`: The URL request to fetch the metadata from.
- `timeout`: The time interval after which the request automatically fails if it hasn’t already completed. By default, this is 30 seconds. If a metadata fetch takes longer than the timeout interval, an `Error` is thrown.
- `includeSubresources`: Determines if subresources should be fetched in addition to the main resource. If `true`, additional data will be fetched from the network to provide subresources such as images and icons. If `false`, no additional networking is done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/linkmetadata/init(fetching:timeout:includesubresources:)-7rkd9)*