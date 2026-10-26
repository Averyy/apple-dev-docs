---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence/flatmaplatest(_:)-1ymrb"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# flatMapLatest(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.flatMapLatest(_:)`.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func flatMapLatest<T>(_ transform: @escaping @Sendable (Self.Element) -> T) -> some Sendable & AsyncSequence<T.Element, T.Failure> where T : Sendable, T : AsyncSequence, Self.Element : Sendable, Self.Failure == Never, T.Element : Sendable
```

Available when `Self` conforms to `Sendable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence/flatmaplatest(_:)-1ymrb)*