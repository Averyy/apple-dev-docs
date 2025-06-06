# filter(_:)

**Framework**: Swift  
**Kind**: method

Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.

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
func filter(_ isIncluded: (Dictionary<Key, Value>.Element) throws -> Bool) rethrows -> [Key : Value]
```

#### Return Value

A dictionary of the key-value pairs that `isIncluded` allows.

## Parameters

- `isIncluded`: A closure that takes a key-value pair as its   argument and returns a Boolean value indicating whether the pair   should be included in the returned dictionary.

## See Also

- [func removeValue(forKey: Key) -> Value?](dictionary/removevalue(forkey:).md)
  Removes the given key and its associated value from the dictionary.
- [func remove(at: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/remove(at:).md)
  Removes and returns the key-value pair at the specified index.
- [func removeAll(keepingCapacity: Bool)](dictionary/removeall(keepingcapacity:).md)
  Removes all key-value pairs from the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/filter(_:))*