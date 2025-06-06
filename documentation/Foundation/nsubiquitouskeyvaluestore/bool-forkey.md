# bool(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the Boolean value associated with the specified key.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func bool(forKey aKey: String) -> Bool
```

#### Return Value

If a Boolean value is associated with the specified key, that value is returned. If the key was not found, this method returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `aKey`: A key in the key-value store.

## See Also

- [func set(Bool, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-8o8mq.md)
  Sets a Boolean value for the specified key in the key-value store.
- [func array(forKey: String) -> [Any]?](nsubiquitouskeyvaluestore/array(forkey:).md)
  Returns the array associated with the specified key.
- [func data(forKey: String) -> Data?](nsubiquitouskeyvaluestore/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](nsubiquitouskeyvaluestore/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.
- [func double(forKey: String) -> Double](nsubiquitouskeyvaluestore/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func longLong(forKey: String) -> Int64](nsubiquitouskeyvaluestore/longlong(forkey:).md)
  Returns the `long long` value associated with the specified key.
- [func object(forKey: String) -> Any?](nsubiquitouskeyvaluestore/object(forkey:).md)
  Returns the object associated with the specified key.
- [func string(forKey: String) -> String?](nsubiquitouskeyvaluestore/string(forkey:).md)
  Returns the string associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/bool(forkey:))*