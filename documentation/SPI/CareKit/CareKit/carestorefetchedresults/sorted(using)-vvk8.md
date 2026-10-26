---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/sorted(using:)-vvk8"
framework: "CareKit/CareKit"
---

# sorted(using:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.sorted(using:)`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
func sorted<S, Comparator>(using comparators: S) -> [Self.Element] where S : Sequence, Comparator : SortComparator, Comparator == S.Element, Self.Element == Comparator.Compared
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/sorted(using:)-vvk8)*