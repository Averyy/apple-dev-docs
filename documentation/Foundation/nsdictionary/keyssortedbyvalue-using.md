# keysSortedByValue(using:)

**Framework**: Foundation  
**Kind**: method

Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.

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
func keysSortedByValue(using comparator: Selector) -> [Any]
```

#### Return Value

An array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.

#### Discussion

Pairs of dictionary values are compared using the comparison method specified by `comparator`; the `comparator` message is sent to one of the values and has as its single argument the other value from the dictionary.

## Parameters

- `comparator`: The   method should return   if the dictionary value is smaller than the argument,   if the dictionary value is larger than the argument, and   if they are equal.

## See Also

- [var allKeys: [Any]](nsdictionary/allkeys.md)
  A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [func sortedArray(using: Selector) -> [Any]](nsarray/sortedarray(using:)-9nhh9.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [func keysSortedByValue(comparator: (Any, Any) -> ComparisonResult) -> [Any]](nsdictionary/keyssortedbyvalue(comparator:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.
- [func keysSortedByValue(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](nsdictionary/keyssortedbyvalue(options:usingcomparator:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/keyssortedbyvalue(using:))*