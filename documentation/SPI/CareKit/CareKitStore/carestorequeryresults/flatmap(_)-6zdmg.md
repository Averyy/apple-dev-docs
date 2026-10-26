---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/flatmap(_:)-6zdmg"
framework: "CareKit/CareKitStore"
---

# flatMap(_:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.flatMap(_:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func flatMap<SegmentOfResult>(_ transform: @escaping @Sendable (Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult> where SegmentOfResult : AsyncSequence
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/flatmap(_:)-6zdmg)*