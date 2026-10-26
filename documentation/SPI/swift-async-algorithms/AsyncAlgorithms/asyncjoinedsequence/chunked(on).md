---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedsequence/chunked(on:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunked(on:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks on the uniqueness of a given subject.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked<Subject>(on projection: @escaping @Sendable (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, [Self.Element]> where Subject : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedsequence/chunked(on:))*