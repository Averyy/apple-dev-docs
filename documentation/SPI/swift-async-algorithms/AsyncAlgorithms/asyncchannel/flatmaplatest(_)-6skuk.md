---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchannel/flatmaplatest(_:)-6skuk"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# flatMapLatest(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Transforms elements into new asynchronous sequences, emitting elements from the most recent inner sequence.

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
func flatMapLatest<T>(_ transform: @escaping @Sendable (Element) -> T) -> some AsyncSequence<T.Element, T.Failure> & Sendable where T : Sendable, T : AsyncSequence, Self.Element : Sendable, Self.Failure == T.Failure, T.Element : Sendable
```

Available when `Self` conforms to `Sendable`.

## Discussion

When a new element is emitted by this sequence, the `transform` is called to produce a new inner sequence. Iteration on the previous inner sequence is cancelled, and iteration begins on the new one.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchannel/flatmaplatest(_:)-6skuk)*