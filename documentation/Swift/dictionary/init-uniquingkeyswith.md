# init(_:uniquingKeysWith:)

**Framework**: Swift  
**Kind**: init

Creates a new dictionary from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init<S>(_ keysAndValues: S, uniquingKeysWith combine: (Value, Value) throws -> Value) rethrows where S : Sequence, S.Element == (Key, Value)
```

#### Discussion

You use this initializer to create a dictionary when you have a sequence of key-value tuples that might have duplicate keys. As the dictionary is built, the initializer calls the `combine` closure with the current and new values for any duplicate keys. Pass a closure as `combine` that returns the value to use in the resulting dictionary: The closure can choose between the two values, combine them to produce a new value, or even throw an error.

The following example shows how to choose the first and last values for any duplicate keys:

```swift
let pairsWithDuplicateKeys = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]

let firstValues = Dictionary(pairsWithDuplicateKeys,
                             uniquingKeysWith: { (first, _) in first })
// ["b": 2, "a": 1]

let lastValues = Dictionary(pairsWithDuplicateKeys,
                            uniquingKeysWith: { (_, last) in last })
// ["b": 4, "a": 3]
```

## Parameters

- `keysAndValues`: A sequence of key-value pairs to use for the new   dictionary.
- `combine`: A closure that is called with the values for any duplicate   keys that are encountered. The closure returns the desired value for   the final dictionary.

## See Also

- [init()](dictionary/init.md)
  Creates an empty dictionary.
- [init(minimumCapacity: Int)](dictionary/init(minimumcapacity:).md)
  Creates an empty dictionary with preallocated space for at least the specified number of elements.
- [init<S>(uniqueKeysWithValues: S)](dictionary/init(uniquekeyswithvalues:).md)
  Creates a new dictionary from the key-value pairs in the given sequence.
- [init<S>(grouping: S, by: (S.Element) throws -> Key) rethrows](dictionary/init(grouping:by:).md)
  Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/init(_:uniquingkeyswith:))*