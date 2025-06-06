# init(upstream:predicate:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.

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
init(upstream: Upstream, predicate: @escaping (Publishers.TryRemoveDuplicates<Upstream>.Output, Publishers.TryRemoveDuplicates<Upstream>.Output) throws -> Bool)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `predicate`: An error-throwing closure to evaluate whether two elements are equivalent, for purposes of filtering. Return   from this closure to indicate that the second element is a duplicate of the first. If this closure throws an error, the publisher terminates with the thrown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryremoveduplicates/init(upstream:predicate:))*