---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/compactmap(_:)-6tp8p"
framework: "CareKit/CareKitStore"
---

# compactMap(_:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.compactMap(_:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func compactMap<ElementOfResult>(_ transform: @escaping @Sendable (Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/compactmap(_:)-6tp8p)*