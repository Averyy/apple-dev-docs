# sort(_:context:)

**Framework**: Foundation  
**Kind**: method

Sorts the receiver in ascending order as defined by the comparison function `compare`.

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
func sort(_ compare: (Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)
```

#### Discussion

This approach allows the comparison to be based on some outside parameter, such as whether character sorting is case sensitive or case insensitive.

## Parameters

- `compare`: The function’s parameters are two objects to compare and the context parameter,  . The function should return   if the first element is smaller than the second,   if the first element is larger than the second, and   if the elements are equal.
- `context`: The context argument to be passed to the compare function.

## See Also

- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]](nsarray/sortedarray(_:context:).md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func exchangeObject(at: Int, withObjectAt: Int)](nsmutablearray/exchangeobject(at:withobjectat:).md)
  Exchanges the objects in the array at given indexes.
- [func sort(using: [NSSortDescriptor])](nsmutablearray/sort(using:)-4eh07.md)
  Sorts the receiver using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(comparator:).md)
  Sorts the receiver in ascending order using the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(options:usingcomparator:).md)
  Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort(using: Selector)](nsmutablearray/sort(using:)-537vs.md)
  Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/sort(_:context:))*