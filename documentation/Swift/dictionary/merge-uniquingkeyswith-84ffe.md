# merge(_:uniquingKeysWith:)

**Framework**: Swift  
**Kind**: method

Merges the key-value pairs in the given sequence into the dictionary, using a combining closure to determine the value for any duplicate keys.

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
mutating func merge<S, E>(_ other: S, uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) where S : Sequence, E : Error, S.Element == (Key, Value)
```

#### Discussion

Use the `combine` closure to select a value to use in the updated dictionary, or to combine existing and new values. As the key-value pairs are merged with the dictionary, the `combine` closure is called with the current and new values for any duplicate keys that are encountered.

This example shows how to choose the current or new values for any duplicate keys:

```swift
var dictionary = ["a": 1, "b": 2]

// Keeping existing value for key "a":
dictionary.merge(zip(["a", "c"], [3, 4])) { (current, _) in current }
// ["b": 2, "a": 1, "c": 4]

// Taking the new value for key "a":
dictionary.merge(zip(["a", "d"], [5, 6])) { (_, new) in new }
// ["b": 2, "a": 5, "c": 4, "d": 6]
```

## Parameters

- `other`: A sequence of key-value pairs.
- `combine`: A closure that takes the current and new values for any duplicate keys. The closure returns the desired value for the final dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/merge(_:uniquingkeyswith:)-84ffe)*