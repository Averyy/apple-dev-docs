# init(upstream:retries:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that attempts to recreate its subscription to a failed upstream publisher.

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
init(upstream: Upstream, retries: Int?)
```

## Parameters

- `upstream`: The publisher from which this publisher receives its elements.
- `retries`: The maximum number of retry attempts to perform. If  , this publisher attempts to reconnect with the upstream publisher an unlimited number of times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/retry/init(upstream:retries:))*