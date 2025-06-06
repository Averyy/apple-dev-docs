# sort(options:usingComparator:)

**Framework**: Foundation  
**Kind**: method

Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.

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
func sort(options opts: NSSortOptions = [], usingComparator cmptr: (Any, Any) -> ComparisonResult)
```

## Parameters

- `opts`: A bitmask that specifies the options for the sort (whether it should be performed concurrently and whether it should be performed stably).
- `cmptr`: A comparator block.

## See Also

- [func sort(using: [NSSortDescriptor])](nsmutableorderedset/sort(using:).md)
  Sorts the receiving ordered set using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sort(comparator:).md)
  Sorts the mutable ordered set using the comparison method specified by the comparator block.
- [func sortRange(NSRange, options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sortrange(_:options:usingcomparator:).md)
  Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/sort(options:usingcomparator:))*