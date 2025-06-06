# init(upstream:decoder:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that decodes elements received from an upstream publisher, using a given decoder.

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
init(upstream: Upstream, decoder: Coder)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `decoder`: The decoder that decodes elements received from the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/decode/init(upstream:decoder:))*