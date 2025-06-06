# sortedArray(options:usingComparator:)

**Framework**: Foundation  
**Kind**: method

Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.

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
func sortedArray(options opts: NSSortOptions = [], usingComparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]
```

#### Return Value

An array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified `cmptr`.

## Parameters

- `opts`: A bitmask that specifies the options for the sort (whether it should be performed concurrently and whether it should be performed stably).
- `cmptr`: A comparator block.

## See Also

- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](nsorderedset/sortedarray(using:).md)
  Returns an array of the ordered set’s elements sorted as specified by a given array of sort descriptors.
- [func sortedArray(comparator: (Any, Any) -> ComparisonResult) -> [Any]](nsorderedset/sortedarray(comparator:).md)
  Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/sortedarray(options:usingcomparator:))*