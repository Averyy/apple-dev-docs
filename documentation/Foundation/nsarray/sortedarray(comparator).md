# sortedArray(comparator:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.

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
func sortedArray(comparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]
```

```objc
- (NSArray<id> *) sortedArrayUsingComparator:(NSComparator) cmptr;
```

## Return Value

An array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified `cmptr`.

## Parameters

- `cmptr`: A comparator block.

## See Also

### Sorting
- [var sortedArrayHint: Data](./sortedarrayhint.md)
  Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [`sortedArray(_:context:hint:)`](./sortedarray%28_,context,hint%29.md).
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]](./sortedarray%28_,context%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?, hint: Data?) -> [Any]](./sortedarray%28_,context,hint%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](./sortedarray%28using%29-82wi1.md)
  Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [func sortedArray(using: Selector) -> [Any]](./sortedarray%28using%29-9nhh9.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [func sortedArray(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](./sortedarray%28options,usingcomparator%29.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [typealias Comparator](../comparator.md)
  Defines the signature for a block object used for comparison operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/sortedarray(comparator:))*