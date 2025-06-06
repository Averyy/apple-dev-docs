# sortedArray(_:context:)

**Framework**: Foundation  
**Kind**: method

Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.

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
func sortedArray(_ comparator: (Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]
```

#### Discussion

The new array contains references to the receiving array’s elements, not copies of them.

The comparison function is used to compare two elements at a time and should return `NSOrderedAscending` if the first element is smaller than the second, `NSOrderedDescending` if the first element is larger than the second, and `NSOrderedSame` if the elements are equal. Each time the comparison function is called, it’s passed `context` as its third argument. This allows the comparison to be based on some outside parameter, such as whether character sorting is case-sensitive or case-insensitive.

Given `anArray` (an array of `NSNumber` objects) and a comparison function of this type:

```objc
NSInteger intSort(id num1, id num2, void *context)
{
    int v1 = [num1 intValue];
    int v2 = [num2 intValue];
    if (v1 < v2)
        return NSOrderedAscending;
    else if (v1 > v2)
        return NSOrderedDescending;
    else
        return NSOrderedSame;
}
```

A sorted version of `anArray` is created in this way:

```objc
NSArray *sortedArray; sortedArray = [anArray sortedArrayUsingFunction:intSort context:NULL];
```

## See Also

- [var sortedArrayHint: Data](nsarray/sortedarrayhint.md)
  Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [`sortedArray(_:context:hint:)`](nsarray/sortedarray(_:context:hint:).md).
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?, hint: Data?) -> [Any]](nsarray/sortedarray(_:context:hint:).md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](nsarray/sortedarray(using:)-82wi1.md)
  Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [func sortedArray(using: Selector) -> [Any]](nsarray/sortedarray(using:)-9nhh9.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [func sortedArray(comparator: (Any, Any) -> ComparisonResult) -> [Any]](nsarray/sortedarray(comparator:).md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [func sortedArray(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](nsarray/sortedarray(options:usingcomparator:).md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [typealias Comparator](comparator.md)
  Defines the signature for a block object used for comparison operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/sortedarray(_:context:))*