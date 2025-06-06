# removeAll(keepingCapacity:)

**Framework**: Swift  
**Kind**: method

Removes all key-value pairs from the dictionary.

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
mutating func removeAll(keepingCapacity keepCapacity: Bool = false)
```

#### Discussion

Calling this method invalidates all indices with respect to the dictionary.

> **Note**: O(), where  is the number of key-value pairs in the dictionary.

## Parameters

- `keepCapacity`: Whether the dictionary should keep its   underlying buffer. If you pass  , the operation preserves the   buffer capacity that the collection has, otherwise the underlying   buffer is released.  The default is  .

## See Also

- [func filter((Dictionary<Key, Value>.Element) throws -> Bool) rethrows -> [Key : Value]](dictionary/filter(_:).md)
  Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.
- [func removeValue(forKey: Key) -> Value?](dictionary/removevalue(forkey:).md)
  Removes the given key and its associated value from the dictionary.
- [func remove(at: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/remove(at:).md)
  Removes and returns the key-value pair at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/removeall(keepingcapacity:))*