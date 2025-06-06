# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the key-value pair at the specified position.

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
subscript(position: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element { get }
```

#### Return Value

A two-element tuple with the key and value corresponding to `position`.

#### Overview

This subscript takes an index into the dictionary, instead of a key, and returns the corresponding key-value pair as a tuple. When performing collection-based operations that return an index into a dictionary, use this subscript with the resulting value.

For example, to find the key for a particular value in a dictionary, use the `firstIndex(where:)` method.

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana", "JP": "Japan"]
if let index = countryCodes.firstIndex(where: { $0.value == "Japan" }) {
    print(countryCodes[index])
    print("Japan's country code is '\(countryCodes[index].key)'.")
} else {
    print("Didn't find 'Japan' as a value in the dictionary.")
}
// Prints "(key: "JP", value: "Japan")"
// Prints "Japan's country code is 'JP'."
```

## Parameters

- `position`: The position of the key-value pair to access.    must be a valid index of the dictionary and not equal to   .

## See Also

- [subscript(Key) -> Value?](dictionary/subscript(_:)-8rfql.md)
  Accesses the value associated with the given key for reading and writing.
- [subscript(Key, default _: @autoclosure () -> Value) -> Value](dictionary/subscript(_:default:).md)
  Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [func index(forKey: Key) -> Dictionary<Key, Value>.Index?](dictionary/index(forkey:).md)
  Returns the index for the given key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/subscript(_:)-4bhoo)*