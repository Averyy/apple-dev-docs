---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:or:)-778x6"
framework: "CareKit/CareKitStore"
---

# chunks(ofCount:or:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:or:)`.

## Declaration

```swift
func chunks<Signal>(ofCount count: Int, or signal: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Self.Element : Sendable, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:or:)-778x6)*