# sort(using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sorts the receiver using a given array of sort descriptors.

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
func sort(using sortDescriptors: [NSSortDescriptor])
```

```objc
- (void) sortUsingDescriptors:(NSArray<NSSortDescriptor *> *) sortDescriptors;
```

## Discussion

See [`NSSortDescriptor`](../nssortdescriptor.md) for additional information.

## Parameters

- `sortDescriptors`: An array containing the `NSSortDescriptor` objects to use to sort the receiving array’s contents.

## See Also

### Related Documentation
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](../nsarray/sortedarray%28using%29-82wi1.md)
  Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
### Rearranging Content
- [func exchangeObject(at: Int, withObjectAt: Int)](./exchangeobject%28at,withobjectat%29.md)
  Exchanges the objects in the array at given indexes.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](./sort%28comparator%29.md)
  Sorts the receiver in ascending order using the comparison method specified by a given [`Comparator`](../comparator.md) block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](./sort%28options,usingcomparator%29.md)
  Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [`Comparator`](../comparator.md) block.
- [func sort((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](./sort%28_,context%29.md)
  Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [func sort(using: Selector)](./sort%28using%29-537vs.md)
  Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/sort(using:)-4eh07)*