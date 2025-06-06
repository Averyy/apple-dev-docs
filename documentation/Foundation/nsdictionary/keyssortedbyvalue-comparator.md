# keysSortedByValue(comparator:)

**Framework**: Foundation  
**Kind**: method

Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.

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
func keysSortedByValue(comparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]
```

#### Return Value

An array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using `cmptr`.

## Parameters

- `cmptr`: A comparator block.

## See Also

- [func keysSortedByValue(using: Selector) -> [Any]](nsdictionary/keyssortedbyvalue(using:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.
- [func keysSortedByValue(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](nsdictionary/keyssortedbyvalue(options:usingcomparator:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/keyssortedbyvalue(comparator:))*