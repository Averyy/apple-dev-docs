# sort(using:)

**Framework**: Foundation  
**Kind**: method

Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.

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
func sort(using comparator: Selector)
```

## Parameters

- `comparator`: The   message is sent to each object in the array and has as its single argument another object in the array. The   method should return   if the array is smaller than the argument,   if the array is larger than the argument, and   if they are equal.

## See Also

- [func sortedArray(using: Selector) -> [Any]](nsarray/sortedarray(using:)-9nhh9.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [func exchangeObject(at: Int, withObjectAt: Int)](nsmutablearray/exchangeobject(at:withobjectat:).md)
  Exchanges the objects in the array at given indexes.
- [func sort(using: [NSSortDescriptor])](nsmutablearray/sort(using:)-4eh07.md)
  Sorts the receiver using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(comparator:).md)
  Sorts the receiver in ascending order using the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(options:usingcomparator:).md)
  Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](nsmutablearray/sort(_:context:).md)
  Sorts the receiver in ascending order as defined by the comparison function `compare`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/sort(using:)-537vs)*