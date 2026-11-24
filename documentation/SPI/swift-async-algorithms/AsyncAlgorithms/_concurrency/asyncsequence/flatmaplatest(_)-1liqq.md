---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/_concurrency/asyncsequence/flatmaplatest(_:)-1liqq"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# flatMapLatest(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func flatMapLatest<T>(_ transform: @escaping @Sendable (Element) -> T) -> some AsyncSequence<T.Element, Failure> & Sendable where T : Sendable, T : AsyncSequence, Self.Element : Sendable, T.Element : Sendable, T.Failure == Never
```

Available when `Self` conforms to `Sendable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/_concurrency/asyncsequence/flatmaplatest(_:)-1liqq)*