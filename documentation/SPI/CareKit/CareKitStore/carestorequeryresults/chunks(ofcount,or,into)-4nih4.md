---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:or:into:)-4nih4"
framework: "CareKit/CareKitStore"
---

# chunks(ofCount:or:into:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:or:into:)`.

## Declaration

```swift
func chunks<Signal, Collected>(ofCount count: Int, or signal: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:or:into:)-4nih4)*