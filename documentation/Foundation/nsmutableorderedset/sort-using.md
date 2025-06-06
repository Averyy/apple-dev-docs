# sort(using:)

**Framework**: Foundation  
**Kind**: method

Sorts the receiving ordered set using a given array of sort descriptors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sort(using sortDescriptors: [NSSortDescriptor])
```

#### Discussion

See [`NSSortDescriptor`](nssortdescriptor.md) for additional information.

## Parameters

- `sortDescriptors`: An array containing the   objects to use to sort the receiving ordered set’s contents.

## See Also

- [func sort(comparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sort(comparator:).md)
  Sorts the mutable ordered set using the comparison method specified by the comparator block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sort(options:usingcomparator:).md)
  Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
- [func sortRange(NSRange, options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sortrange(_:options:usingcomparator:).md)
  Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/sort(using:))*