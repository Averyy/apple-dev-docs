---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchannel/drop(while:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# drop(while:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.drop(while:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func drop(while predicate: @escaping @Sendable (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchannel/drop(while:))*