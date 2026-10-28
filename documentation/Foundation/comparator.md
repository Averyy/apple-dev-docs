# Comparator

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

Defines the signature for a block object used for comparison operations.

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
typealias Comparator = (Any, Any) -> ComparisonResult
```

```c
typedef enum NSComparisonResult (^)(id, id) NSComparator;
```

## Discussion

The arguments to the [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) are two objects to compare. The block returns an [`ComparisonResult`](./comparisonresult.md) value to denote the ordering of the two objects.

You use `NSComparator` blocks in comparison operations such as `NSArray`’s [`sortedArray(comparator:)`](./nsarray/sortedarray%28comparator%29.md), for example:

```objc
NSArray *sortedArray = [array sortedArrayUsingComparator: ^(id obj1, id obj2) {
 
    if ([obj1 integerValue] > [obj2 integerValue]) {
        return (NSComparisonResult)NSOrderedDescending;
    }
 
    if ([obj1 integerValue] < [obj2 integerValue]) {
        return (NSComparisonResult)NSOrderedAscending;
    }
    return (NSComparisonResult)NSOrderedSame;
}];
```

## See Also

### Sorting
- [var sortedArrayHint: Data](./nsarray/sortedarrayhint.md)
  Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [`sortedArray(_:context:hint:)`](./nsarray/sortedarray%28_,context,hint%29.md).
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]](./nsarray/sortedarray%28_,context%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?, hint: Data?) -> [Any]](./nsarray/sortedarray%28_,context,hint%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](./nsarray/sortedarray%28using%29-82wi1.md)
  Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [func sortedArray(using: Selector) -> [Any]](./nsarray/sortedarray%28using%29-9nhh9.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [func sortedArray(comparator: (Any, Any) -> ComparisonResult) -> [Any]](./nsarray/sortedarray%28comparator%29.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [func sortedArray(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](./nsarray/sortedarray%28options,usingcomparator%29.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/comparator)*