# removeValue(forKey:)

**Framework**: Swift  
**Kind**: method

Removes the given key and its associated value from the dictionary.

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
@discardableResult
mutating func removeValue(forKey key: Key) -> Value?
```

#### Return Value

The value that was removed, or `nil` if the key was not present in the dictionary.

#### Discussion

If the key is found in the dictionary, this method returns the key’s associated value. On removal, this method invalidates all indices with respect to the dictionary.

```swift
var hues = ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156]
if let value = hues.removeValue(forKey: "Coral") {
    print("The value \(value) was removed.")
}
// Prints "The value 16 was removed."
```

If the key isn’t found in the dictionary, `removeValue(forKey:)` returns `nil`.

```swift
if let value = hues.removeValue(forKey: "Cerise") {
    print("The value \(value) was removed.")
} else {
    print("No value found for that key.")
}
// Prints "No value found for that key."
```

> **Note**: O(), where  is the number of key-value pairs in the dictionary.

## Parameters

- `key`: The key to remove along with its associated value.

## See Also

- [func filter((Dictionary<Key, Value>.Element) throws -> Bool) rethrows -> [Key : Value]](dictionary/filter(_:).md)
  Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.
- [func remove(at: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/remove(at:).md)
  Removes and returns the key-value pair at the specified index.
- [func removeAll(keepingCapacity: Bool)](dictionary/removeall(keepingcapacity:).md)
  Removes all key-value pairs from the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/removevalue(forkey:))*