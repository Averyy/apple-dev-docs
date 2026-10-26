---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/reduce(into:_:)"
framework: "CareKit/CareKitStore"
---

# reduce(into:_:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reduce(into:_:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reduce<Result>(into initialResult: Result, _ updateAccumulatingResult: (inout Result, Self.Element) async throws -> Void) async rethrows -> Result
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/reduce(into:_:))*