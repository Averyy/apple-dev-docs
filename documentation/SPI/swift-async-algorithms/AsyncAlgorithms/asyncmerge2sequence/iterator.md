---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncmerge2sequence/iterator"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncMerge2Sequence.Iterator

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct Iterator
```

Available when `Base1` conforms to `Sendable`, `Base1` conforms to `AsyncSequence`, `Base2` conforms to `Sendable`, `Base2` conforms to `AsyncSequence`, `Base1.Element` conforms to `Sendable`, and `Base1.Element` is `Base2.Element`.

## Topics

### Instance Methods
- [func next() async rethrows -> AsyncMerge2Sequence<Base1, Base2>.Element?](./iterator/next%28%29.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](./iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- _Concurrency.AsyncIteratorProtocol


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncmerge2sequence/iterator)*