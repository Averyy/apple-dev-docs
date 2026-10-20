# sort(comparator:)

**Framework**: Foundation  
**Kind**: method

Sorts the receiver in ascending order using the comparison method specified by a given [`Comparator`](comparator.md) block.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
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

- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](nsarray/sortedarray(using:)-82wi1.md)
  Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [func exchangeObject(at: Int, withObjectAt: Int)](nsmutablearray/exchangeobject(at:withobjectat:).md)
  Exchanges the objects in the array at given indexes.
- [func sort(using: [NSSortDescriptor])](nsmutablearray/sort(using:)-4eh07.md)
  Sorts the receiver using a given array of sort descriptors.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(options:usingcomparator:).md)
  Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](nsmutablearray/sort(_:context:).md)
  Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [func sort(using: Selector)](nsmutablearray/sort(using:)-537vs.md)
  Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/sort(comparator:))*