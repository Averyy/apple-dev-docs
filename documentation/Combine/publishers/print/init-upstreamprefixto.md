# init(upstream:prefix:to:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that prints log messages for all publishing events.

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
init(upstream: Upstream, prefix: String, to stream: (any TextOutputStream)? = nil)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `prefix`: A string with which to prefix all log messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/print/init(upstream:prefix:to:))*