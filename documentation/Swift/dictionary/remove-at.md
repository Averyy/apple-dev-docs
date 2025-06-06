# remove(at:)

**Framework**: Swift  
**Kind**: method

Removes and returns the key-value pair at the specified index.

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
mutating func remove(at index: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element
```

#### Return Value

The key-value pair that correspond to `index`.

#### Discussion

Calling this method invalidates any existing indices for use with this dictionary.

> **Note**: O(), where  is the number of key-value pairs in the dictionary.

O(), where  is the number of key-value pairs in the dictionary.

## Parameters

- `index`: The position of the key-value pair to remove.    must be a valid index of the dictionary, and must not equal the   dictionary’s end index.

## See Also

- [func filter((Dictionary<Key, Value>.Element) throws -> Bool) rethrows -> [Key : Value]](dictionary/filter(_:).md)
  Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.
- [func removeValue(forKey: Key) -> Value?](dictionary/removevalue(forkey:).md)
  Removes the given key and its associated value from the dictionary.
- [func removeAll(keepingCapacity: Bool)](dictionary/removeall(keepingcapacity:).md)
  Removes all key-value pairs from the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/remove(at:))*