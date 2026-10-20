# filter(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
consuming func filter<E>(_ isIncluded: (Dictionary<Key, Value>.Element) throws(E) -> Bool) throws(E) -> [Key : Value] where E : Error
```

Available when `Key` conforms to `Hashable`.

#### Return Value

A dictionary of the key-value pairs that `isIncluded` allows.

## Parameters

- `isIncluded`: A closure that takes a key-value pair as its argument and returns a Boolean value indicating whether the pair should be included in the returned dictionary.

## See Also

### Removing Keys and Values
- [func removeValue(forKey: Key) -> Value?](./removevalue%28forkey%29.md)
  Removes the given key and its associated value from the dictionary.
- [func remove(at: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](./remove%28at%29.md)
  Removes and returns the key-value pair at the specified index.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29.md)
  Removes all key-value pairs from the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/filter(_:))*