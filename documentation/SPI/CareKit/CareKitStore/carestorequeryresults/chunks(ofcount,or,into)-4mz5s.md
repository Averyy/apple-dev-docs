---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:or:into:)-4mz5s"
framework: "CareKit/CareKitStore"
---

# chunks(ofCount:or:into:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:or:into:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func chunks<C, Collected>(ofCount count: Int, or timer: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>> where Self : Sendable, C : Clock, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/chunks(ofcount:or:into:)-4mz5s)*