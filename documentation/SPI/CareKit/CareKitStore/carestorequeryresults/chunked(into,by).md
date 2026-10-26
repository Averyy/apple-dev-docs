---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunked(into:by:)"
framework: "CareKit/CareKitStore"
---

# chunked(into:by:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunked(into:by:)`.

## Declaration

```swift
func chunked<Collected>(into: Collected.Type, by belongInSameGroup: @escaping @Sendable (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, Collected> where Collected : RangeReplaceableCollection, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunked(into:by:))*