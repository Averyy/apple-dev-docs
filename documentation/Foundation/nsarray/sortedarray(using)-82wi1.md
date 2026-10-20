# sortedArray(using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.

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
func sortedArray(using sortDescriptors: [NSSortDescriptor]) -> [Any]
```

```objc
- (NSArray<id> *) sortedArrayUsingDescriptors:(NSArray<NSSortDescriptor *> *) sortDescriptors;
```

#### Return Value

A copy of the receiving array sorted as specified by `sortDescriptors`.

#### Discussion

The first descriptor specifies the primary key path to be used in sorting the receiving array’s contents. Any subsequent descriptors are used to further refine sorting of objects with duplicate values. See [`NSSortDescriptor`](../nssortdescriptor.md) for additional information.

## Parameters

- `sortDescriptors`: An array of `NSSortDescriptor` objects.

## See Also

### Sorting
- [var sortedArrayHint: Data](./sortedarrayhint.md)
  Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [`sortedArray(_:context:hint:)`](./sortedarray%28_,context,hint%29.md).
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]](./sortedarray%28_,context%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?, hint: Data?) -> [Any]](./sortedarray%28_,context,hint%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray(using: Selector) -> [Any]](./sortedarray%28using%29-9nhh9.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [func sortedArray(comparator: (Any, Any) -> ComparisonResult) -> [Any]](./sortedarray%28comparator%29.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [func sortedArray(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](./sortedarray%28options,usingcomparator%29.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [typealias Comparator](../comparator.md)
  Defines the signature for a block object used for comparison operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/sortedarray(using:)-82wi1)*