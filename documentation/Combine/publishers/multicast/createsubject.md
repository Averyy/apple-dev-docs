# createSubject

**Framework**: Combine  
**Kind**: property

A closure that returns a subject each time a subscriber attaches to the multicast publisher.

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
final let createSubject: () -> SubjectType
```

## See Also

- [let upstream: Upstream](publishers/multicast/upstream.md)
  The publisher from which this publisher receives its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/multicast/createsubject)*