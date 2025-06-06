# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the value associated with the given key for reading and writing.

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
subscript(key: Key) -> Value? { get set }
```

#### Return Value

The value associated with `key` if `key` is in the dictionary; otherwise, `nil`.

#### Overview

This  subscript returns the value for the given key if the key is found in the dictionary, or `nil` if the key is not found.

The following example creates a new dictionary and prints the value of a key found in the dictionary (`"Coral"`) and a key not found in the dictionary (`"Cerise"`).

```swift
var hues = ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156]
print(hues["Coral"])
// Prints "Optional(16)"
print(hues["Cerise"])
// Prints "nil"
```

When you assign a value for a key and that key already exists, the dictionary overwrites the existing value. If the dictionary doesn’t contain the key, the key and value are added as a new key-value pair.

Here, the value for the key `"Coral"` is updated from `16` to `18` and a new key-value pair is added for the key `"Cerise"`.

```swift
hues["Coral"] = 18
print(hues["Coral"])
// Prints "Optional(18)"

hues["Cerise"] = 330
print(hues["Cerise"])
// Prints "Optional(330)"
```

If you assign `nil` as the value for the given key, the dictionary removes that key and its associated value.

In the following example, the key-value pair for the key `"Aquamarine"` is removed from the dictionary by assigning `nil` to the key-based subscript.

```swift
hues["Aquamarine"] = nil
print(hues)
// Prints "["Coral": 18, "Heliotrope": 296, "Cerise": 330]"
```

## Parameters

- `key`: The key to find in the dictionary.

## See Also

- [subscript(Key, default _: @autoclosure () -> Value) -> Value](dictionary/subscript(_:default:).md)
  Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [func index(forKey: Key) -> Dictionary<Key, Value>.Index?](dictionary/index(forkey:).md)
  Returns the index for the given key.
- [subscript(Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/subscript(_:)-4bhoo.md)
  Accesses the key-value pair at the specified position.
- [var keys: Dictionary<Key, Value>.Keys](dictionary/keys-swift.property.md)
  A collection containing just the keys of the dictionary.
- [var values: Dictionary<Key, Value>.Values](dictionary/values-swift.property.md)
  A collection containing just the values of the dictionary.
- [var first: Self.Element?](dictionary/first.md)
  The first element of the collection.
- [func randomElement() -> Self.Element?](dictionary/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](dictionary/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/subscript(_:)-8rfql)*