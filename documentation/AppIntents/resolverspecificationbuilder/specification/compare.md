# compare(_:_:)

**Framework**: App Intents  
**Kind**: method

If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func compare<Comparator>(_ lhs: Comparator.Compared, _ rhs: Comparator.Compared) -> ComparisonResult where Comparator : SortComparator, Comparator == Self.Element
```

#### Discussion

The first element of the sequence of comparators specifies the primary comparator to be used in sorting the sequence’s elements. Any subsequent comparators are used to further refine the order of elements with equal values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolverspecificationbuilder/specification/compare(_:_:))*