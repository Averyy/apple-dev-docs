# init(upstream:createSubject:)

**Framework**: Combine  
**Kind**: init

Creates a multicast publisher that applies a closure to create a subject that delivers elements to subscribers.

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
init(upstream: Upstream, createSubject: @escaping () -> SubjectType)
```

## Parameters

- `createSubject`: A closure that returns a   each time a subscriber attaches to the multicast publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/multicast/init(upstream:createsubject:))*