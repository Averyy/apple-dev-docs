# init(uniqueKeysWithValues:)

**Framework**: Swift  
**Kind**: init

Creates a new dictionary from the key-value pairs in the given sequence.

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
init<S>(uniqueKeysWithValues keysAndValues: S) where S : Sequence, S.Element == (Key, Value)
```

#### Return Value

A new dictionary initialized with the elements of `keysAndValues`.

#### Discussion

You use this initializer to create a dictionary when you have a sequence of key-value tuples with unique keys. Passing a sequence with duplicate keys to this initializer results in a runtime error. If your sequence might have duplicate keys, use the `Dictionary(_:uniquingKeysWith:)` initializer instead.

The following example creates a new dictionary using an array of strings as the keys and the integers in a countable range as the values:

```swift
let digitWords = ["one", "two", "three", "four", "five"]
let wordToValue = Dictionary(uniqueKeysWithValues: zip(digitWords, 1...5))
print(wordToValue["three"]!)
// Prints "3"
print(wordToValue)
// Prints "["three": 3, "four": 4, "five": 5, "one": 1, "two": 2]"
```

> **Note**: The sequence must not have duplicate keys.

## Parameters

- `keysAndValues`: A sequence of key-value pairs to use for   the new dictionary. Every key in   must be unique.

## See Also

- [init()](dictionary/init.md)
  Creates an empty dictionary.
- [init(minimumCapacity: Int)](dictionary/init(minimumcapacity:).md)
  Creates an empty dictionary with preallocated space for at least the specified number of elements.
- [init<S>(S, uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/init(_:uniquingkeyswith:).md)
  Creates a new dictionary from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.
- [init<S>(grouping: S, by: (S.Element) throws -> Key) rethrows](dictionary/init(grouping:by:).md)
  Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/init(uniquekeyswithvalues:))*