# init(upstream:output:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that replaces any errors in the stream with a provided element.

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
init(upstream: Upstream, output: Publishers.ReplaceError<Upstream>.Output)
```

## Parameters

- `upstream`: The element with which to replace errors from the upstream publisher.
- `output`: The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/replaceerror/init(upstream:output:))*