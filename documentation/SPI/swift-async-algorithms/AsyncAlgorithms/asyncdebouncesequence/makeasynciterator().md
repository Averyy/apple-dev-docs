---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncdebouncesequence/makeasynciterator()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# makeAsyncIterator()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.makeAsyncIterator()`.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func makeAsyncIterator() -> AsyncDebounceSequence<Base, C>.Iterator
```

Available when `Base` conforms to `Sendable`, `Base` conforms to `AsyncSequence`, `C` conforms to `Clock`, and `Base.Element` conforms to `Sendable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncdebouncesequence/makeasynciterator())*