---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/difference(from:)"
framework: "CareKit/CareKit"
---

# difference(from:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inherited from `BidirectionalCollection.difference(from:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func difference<C>(from other: C) -> CollectionDifference<Self.Element> where C : BidirectionalCollection, Self.Element == C.Element
```

Available when `Element` conforms to `Equatable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/difference(from:))*