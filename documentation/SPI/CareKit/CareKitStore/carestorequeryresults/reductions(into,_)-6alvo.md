---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/reductions(into:_:)-6alvo"
framework: "CareKit/CareKitStore"
---

# reductions(into:_:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reductions(into:_:)`.

## Declaration

```swift
func reductions<Result>(into initial: Result, _ transform: @escaping @Sendable (inout Result, Self.Element) async throws -> Void) -> AsyncThrowingExclusiveReductionsSequence<Self, Result>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/reductions(into:_:)-6alvo)*