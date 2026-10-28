# sortedArray(using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of the ordered set’s elements sorted as specified by a given array of sort descriptors.

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
func sortedArray(using sortDescriptors: [NSSortDescriptor]) -> [Any]
```

```objc
- (NSArray<id> *) sortedArrayUsingDescriptors:(NSArray<NSSortDescriptor *> *) sortDescriptors;
```

## Return Value

An `NSArray` containing the ordered set’s elements sorted as specified by `sortDescriptors`.

## Discussion

The first descriptor specifies the primary key path to be used in sorting the ordered set’s elements. Any subsequent descriptors are used to further refine sorting of objects with duplicate values. See [`NSSortDescriptor`](../nssortdescriptor.md) for additional information.

## Parameters

- `sortDescriptors`: An array of [`NSSortDescriptor`](../nssortdescriptor.md) objects.

## See Also

### Creating a Sorted Array
- [func sortedArray(comparator: (Any, Any) -> ComparisonResult) -> [Any]](./sortedarray%28comparator%29.md)
  Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block
- [func sortedArray(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](./sortedarray%28options,usingcomparator%29.md)
  Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/sortedarray(using:))*