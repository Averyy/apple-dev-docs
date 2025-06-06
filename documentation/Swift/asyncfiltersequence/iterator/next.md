# next()

**Framework**: Swift  
**Kind**: method

Produces the next element in the filter sequence.

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
mutating func next() async rethrows -> Base.Element?
```

#### Discussion

This iterator calls `next()` on its base iterator; if this call returns `nil`, `next()` returns nil. Otherwise, `next()` evaluates the result with the `predicate` closure. If the closure returns `true`, `next()` returns the received element; otherwise it awaits the next element from the base iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncfiltersequence/iterator/next())*