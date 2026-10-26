---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunked(by:into:)-7jb7o"
framework: "CareKit/CareKitStore"
---

# chunked(by:into:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunked(by:into:)`.

## Declaration

```swift
func chunked<Signal, Collected>(by signal: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunked(by:into:)-7jb7o)*