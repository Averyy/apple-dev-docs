---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:or:)-1o4f5"
framework: "CareKit/CareKitStore"
---

# chunks(ofCount:or:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:or:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func chunks<C>(ofCount count: Int, or timer: AsyncTimerSequence<C>) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], AsyncTimerSequence<C>> where Self : Sendable, C : Clock, Self.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:or:)-1o4f5)*