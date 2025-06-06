# exchangeObject(at:withObjectAt:)

**Framework**: Foundation  
**Kind**: method

Exchanges the objects in the array at given indexes.

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
func exchangeObject(at idx1: Int, withObjectAt idx2: Int)
```

## Parameters

- `idx1`: The index of the object with which to replace the object at index  .
- `idx2`: The index of the object with which to replace the object at index  .

## See Also

- [func sort(using: [NSSortDescriptor])](nsmutablearray/sort(using:)-4eh07.md)
  Sorts the receiver using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(comparator:).md)
  Sorts the receiver in ascending order using the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(options:usingcomparator:).md)
  Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](nsmutablearray/sort(_:context:).md)
  Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [func sort(using: Selector)](nsmutablearray/sort(using:)-537vs.md)
  Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/exchangeobject(at:withobjectat:))*