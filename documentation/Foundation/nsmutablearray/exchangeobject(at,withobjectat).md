# exchangeObject(at:withObjectAt:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) exchangeObjectAtIndex:(NSUInteger) idx1 withObjectAtIndex:(NSUInteger) idx2;
```

## Parameters

- `idx1`: The index of the object with which to replace the object at index `idx2`.
- `idx2`: The index of the object with which to replace the object at index `idx1`.

## See Also

### Rearranging Content
- [func sort(using: [NSSortDescriptor])](./sort%28using%29-4eh07.md)
  Sorts the receiver using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](./sort%28comparator%29.md)
  Sorts the receiver in ascending order using the comparison method specified by a given [`Comparator`](../comparator.md) block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](./sort%28options,usingcomparator%29.md)
  Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [`Comparator`](../comparator.md) block.
- [func sort((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](./sort%28_,context%29.md)
  Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [func sort(using: Selector)](./sort%28using%29-537vs.md)
  Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/exchangeobject(at:withobjectat:))*