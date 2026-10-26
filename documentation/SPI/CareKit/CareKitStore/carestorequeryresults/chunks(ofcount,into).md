---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:into:)"
framework: "CareKit/CareKitStore"
---

# chunks(ofCount:into:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:into:)`.

## Declaration

```swift
func chunks<Collected>(ofCount count: Int, into: Collected.Type) -> AsyncChunksOfCountSequence<Self, Collected> where Collected : RangeReplaceableCollection, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:into:))*