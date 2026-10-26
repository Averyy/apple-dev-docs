---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinclusivereductionssequence/removeduplicates(by:)-2s4lt"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# removeDuplicates(by:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that omits repeated elements by testing them with an error-throwing predicate.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func removeDuplicates(by predicate: @escaping @Sendable (Self.Element, Self.Element) async throws -> Bool) -> AsyncThrowingRemoveDuplicatesSequence<Self>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinclusivereductionssequence/removeduplicates(by:)-2s4lt)*