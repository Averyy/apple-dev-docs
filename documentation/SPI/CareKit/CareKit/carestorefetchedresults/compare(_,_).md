---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/compare(_:_:)"
framework: "CareKit/CareKit"
---

# compare(_:_:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.compare(_:_:)`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
func compare<Comparator>(_ lhs: Comparator.Compared, _ rhs: Comparator.Compared) -> ComparisonResult where Comparator : SortComparator, Comparator == Self.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/compare(_:_:))*