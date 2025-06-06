# init(upstream:output:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that emits a Boolean value when it receives a specific element from its upstream publisher.

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
init(upstream: Upstream, output: Upstream.Output)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `output`: The element to match in the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/contains/init(upstream:output:))*