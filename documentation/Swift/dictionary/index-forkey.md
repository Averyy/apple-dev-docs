# index(forKey:)

**Framework**: Swift  
**Kind**: method

Returns the index for the given key.

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
func index(forKey key: Key) -> Dictionary<Key, Value>.Index?
```

#### Return Value

The index for `key` and its associated value if `key` is in the dictionary; otherwise, `nil`.

#### Discussion

If the given key is found in the dictionary, this method returns an index into the dictionary that corresponds with the key-value pair.

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana", "JP": "Japan"]
let index = countryCodes.index(forKey: "JP")

print("Country code for \(countryCodes[index!].value): '\(countryCodes[index!].key)'.")
// Prints "Country code for Japan: 'JP'."
```

## Parameters

- `key`: The key to find in the dictionary.

## See Also

- [subscript(Key) -> Value?](dictionary/subscript(_:)-8rfql.md)
  Accesses the value associated with the given key for reading and writing.
- [subscript(Key, default _: @autoclosure () -> Value) -> Value](dictionary/subscript(_:default:).md)
  Accesses the value with the given key, falling back to the given default value if the key isn’t found.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/index(forkey:))*