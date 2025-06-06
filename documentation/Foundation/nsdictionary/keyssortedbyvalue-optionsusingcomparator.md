# keysSortedByValue(options:usingComparator:)

**Framework**: Foundation  
**Kind**: method

Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.

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
func keysSortedByValue(options opts: NSSortOptions = [], usingComparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]
```

#### Return Value

An array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using `cmptr` with the options given in `opts`.

## Parameters

- `opts`: A bitmask of sort options.
- `cmptr`: A comparator block.

## See Also

- [func keysSortedByValue(using: Selector) -> [Any]](nsdictionary/keyssortedbyvalue(using:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.
- [func keysSortedByValue(comparator: (Any, Any) -> ComparisonResult) -> [Any]](nsdictionary/keyssortedbyvalue(comparator:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/keyssortedbyvalue(options:usingcomparator:))*