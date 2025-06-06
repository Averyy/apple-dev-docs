# merging(_:uniquingKeysWith:)

**Framework**: Swift  
**Kind**: method

Creates a dictionary by merging key-value pairs in a sequence into the dictionary, using a combining closure to determine the value for duplicate keys.

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
func merging<S>(_ other: S, uniquingKeysWith combine: (Value, Value) throws -> Value) rethrows -> [Key : Value] where S : Sequence, S.Element == (Key, Value)
```

#### Return Value

A new dictionary with the combined keys and values of this dictionary and `other`.

#### Discussion

Use the `combine` closure to select a value to use in the returned dictionary, or to combine existing and new values. As the key-value pairs are merged with the dictionary, the `combine` closure is called with the current and new values for any duplicate keys that are encountered.

This example shows how to choose the current or new values for any duplicate keys:

```swift
let dictionary = ["a": 1, "b": 2]
let newKeyValues = zip(["a", "b"], [3, 4])

let keepingCurrent = dictionary.merging(newKeyValues) { (current, _) in current }
// ["b": 2, "a": 1]
let replacingCurrent = dictionary.merging(newKeyValues) { (_, new) in new }
// ["b": 4, "a": 3]
```

## Parameters

- `other`: A sequence of key-value pairs.
- `combine`: A closure that takes the current and new values for any   duplicate keys. The closure returns the desired value for the final   dictionary.

## See Also

- [func updateValue(Value, forKey: Key) -> Value?](dictionary/updatevalue(_:forkey:).md)
  Updates the value stored in the dictionary for the given key, or adds a new key-value pair if the key does not exist.
- [func merge([Key : Value], uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/merge(_:uniquingkeyswith:)-m2ub.md)
  Merges the given dictionary into this dictionary, using a combining closure to determine the value for any duplicate keys.
- [func merge<S>(S, uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/merge(_:uniquingkeyswith:)-7smbb.md)
  Merges the key-value pairs in the given sequence into the dictionary, using a combining closure to determine the value for any duplicate keys.
- [func merging([Key : Value], uniquingKeysWith: (Value, Value) throws -> Value) rethrows -> [Key : Value]](dictionary/merging(_:uniquingkeyswith:)-3vtfs.md)
  Creates a dictionary by merging the given dictionary into this dictionary, using a combining closure to determine the value for duplicate keys.
- [func reserveCapacity(Int)](dictionary/reservecapacity(_:).md)
  Reserves enough space to store the specified number of key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/merging(_:uniquingkeyswith:)-9bik6)*