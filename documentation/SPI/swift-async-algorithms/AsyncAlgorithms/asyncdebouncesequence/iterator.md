---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncdebouncesequence/iterator"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncDebounceSequence.Iterator

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
struct Iterator
```

Available when `Base` conforms to `Sendable`, `Base` conforms to `AsyncSequence`, `C` conforms to `Clock`, and `Base.Element` conforms to `Sendable`.

## Topics

### Instance Methods
- [func next() async rethrows -> AsyncDebounceSequence<Base, C>.Element?](./iterator/next%28%29.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](./iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- _Concurrency.AsyncIteratorProtocol


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncdebouncesequence/iterator)*