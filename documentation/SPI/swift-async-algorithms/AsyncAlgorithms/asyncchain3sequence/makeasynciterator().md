---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain3sequence/makeasynciterator()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# makeAsyncIterator()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.makeAsyncIterator()`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func makeAsyncIterator() -> AsyncChain3Sequence<Base1, Base2, Base3>.Iterator
```

Available when `Base1` conforms to `AsyncSequence`, `Base2` conforms to `AsyncSequence`, `Base3` conforms to `AsyncSequence`, `Base1.Element` is `Base2.Element`, and `Base2.Element` is `Base3.Element`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain3sequence/makeasynciterator())*