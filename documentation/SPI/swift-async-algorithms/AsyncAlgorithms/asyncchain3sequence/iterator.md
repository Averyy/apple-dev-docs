---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain3sequence/iterator"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncChain3Sequence.Iterator

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

The iterator for a `AsyncChain3Sequence` instance.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct Iterator
```

Available when `Base1` conforms to `AsyncSequence`, `Base2` conforms to `AsyncSequence`, `Base3` conforms to `AsyncSequence`, `Base1.Element` is `Base2.Element`, and `Base2.Element` is `Base3.Element`.

## Topics

### Instance Methods
- [func next() async rethrows -> AsyncChain3Sequence<Base1, Base2, Base3>.Element?](./iterator/next%28%29.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](./iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- _Concurrency.AsyncIteratorProtocol


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain3sequence/iterator)*