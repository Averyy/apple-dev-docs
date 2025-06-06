# sort(comparator:)

**Framework**: Foundation  
**Kind**: method

Sorts the mutable ordered set using the comparison method specified by the comparator block.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sort(comparator cmptr: (Any, Any) -> ComparisonResult)
```

## Parameters

- `cmptr`: A comparator block.

## See Also

- [func sort(using: [NSSortDescriptor])](nsmutableorderedset/sort(using:).md)
  Sorts the receiving ordered set using a given array of sort descriptors.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sort(options:usingcomparator:).md)
  Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
- [func sortRange(NSRange, options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sortrange(_:options:usingcomparator:).md)
  Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/sort(comparator:))*