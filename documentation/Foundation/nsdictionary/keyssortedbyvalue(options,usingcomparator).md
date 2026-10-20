# keysSortedByValue(options:usingComparator:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<id> *) keysSortedByValueWithOptions:(NSSortOptions) opts usingComparator:(NSComparator) cmptr;
```

#### Return Value

An array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using `cmptr` with the options given in `opts`.

## Parameters

- `opts`: A bitmask of sort options.
- `cmptr`: A comparator block.

## See Also

### Sorting Dictionaries
- [func keysSortedByValue(using: Selector) -> [Any]](./keyssortedbyvalue%28using%29.md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.
- [func keysSortedByValue(comparator: (Any, Any) -> ComparisonResult) -> [Any]](./keyssortedbyvalue%28comparator%29.md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/keyssortedbyvalue(options:usingcomparator:))*