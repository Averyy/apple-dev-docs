---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/reductions(_:_:)-6fjt1"
framework: "CareKit/CareKitStore"
---

# reductions(_:_:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reductions(_:_:)`.

## Declaration

```swift
func reductions<Result>(_ initial: Result, _ transform: @escaping @Sendable (Result, Self.Element) async throws -> Result) -> AsyncThrowingExclusiveReductionsSequence<Self, Result>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/reductions(_:_:)-6fjt1)*