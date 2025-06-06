# keys

**Framework**: Swift  
**Kind**: property

A collection containing just the keys of the dictionary.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift 4.0+

## Declaration

```swift
var keys: Dictionary<Key, Value>.Keys { get }
```

#### Discussion

When iterated over, keys appear in this collection in the same order as they occur in the dictionary’s key-value pairs. Each key in the keys collection has a unique value.

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana", "JP": "Japan"]
print(countryCodes)
// Prints "["BR": "Brazil", "JP": "Japan", "GH": "Ghana"]"

for k in countryCodes.keys {
    print(k)
}
// Prints "BR"
// Prints "JP"
// Prints "GH"
```

## See Also

- [subscript(Key) -> Value?](dictionary/subscript(_:)-8rfql.md)
  Accesses the value associated with the given key for reading and writing.
- [subscript(Key, default _: @autoclosure () -> Value) -> Value](dictionary/subscript(_:default:).md)
  Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [func index(forKey: Key) -> Dictionary<Key, Value>.Index?](dictionary/index(forkey:).md)
  Returns the index for the given key.
- [subscript(Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/subscript(_:)-4bhoo.md)
  Accesses the key-value pair at the specified position.
- [var values: Dictionary<Key, Value>.Values](dictionary/values-swift.property.md)
  A collection containing just the values of the dictionary.
- [var first: Self.Element?](dictionary/first.md)
  The first element of the collection.
- [func randomElement() -> Self.Element?](dictionary/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](dictionary/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/keys-swift.property)*