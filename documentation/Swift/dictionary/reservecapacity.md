# reserveCapacity(_:)

**Framework**: Swift  
**Kind**: method

Reserves enough space to store the specified number of key-value pairs.

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
mutating func reserveCapacity(_ minimumCapacity: Int)
```

#### Discussion

If you are adding a known number of key-value pairs to a dictionary, use this method to avoid multiple reallocations. This method ensures that the dictionary has unique, mutable, contiguous storage, with space allocated for at least the requested number of key-value pairs.

Calling the `reserveCapacity(_:)` method on a dictionary with bridged storage triggers a copy to contiguous storage even if the existing storage has room to store `minimumCapacity` key-value pairs.

## Parameters

- `minimumCapacity`: The requested number of key-value pairs to   store.

## See Also

- [func updateValue(Value, forKey: Key) -> Value?](dictionary/updatevalue(_:forkey:).md)
  Updates the value stored in the dictionary for the given key, or adds a new key-value pair if the key does not exist.
- [func merge([Key : Value], uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/merge(_:uniquingkeyswith:)-m2ub.md)
  Merges the given dictionary into this dictionary, using a combining closure to determine the value for any duplicate keys.
- [func merge<S>(S, uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/merge(_:uniquingkeyswith:)-7smbb.md)
  Merges the key-value pairs in the given sequence into the dictionary, using a combining closure to determine the value for any duplicate keys.
- [func merging([Key : Value], uniquingKeysWith: (Value, Value) throws -> Value) rethrows -> [Key : Value]](dictionary/merging(_:uniquingkeyswith:)-3vtfs.md)
  Creates a dictionary by merging the given dictionary into this dictionary, using a combining closure to determine the value for duplicate keys.
- [func merging<S>(S, uniquingKeysWith: (Value, Value) throws -> Value) rethrows -> [Key : Value]](dictionary/merging(_:uniquingkeyswith:)-9bik6.md)
  Creates a dictionary by merging key-value pairs in a sequence into the dictionary, using a combining closure to determine the value for duplicate keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/reservecapacity(_:))*