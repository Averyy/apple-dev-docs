# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets a string object for the specified key in the key-value store.

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
func set(_ aString: String?, forKey aKey: String)
```

## Parameters

- `aString`: The string you want to store. The total size (in bytes) of the string must not exceed the per-key size limits.
- `aKey`: The key under which to store the value. The length of this key must not exceed 64 bytes using UTF8 encoding.

## See Also

- [func set([Any]?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-40a8f.md)
  Sets an array object for the specified key in the key-value store.
- [func set(Bool, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-8o8mq.md)
  Sets a Boolean value for the specified key in the key-value store.
- [func set(Data?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-3ga7z.md)
  Sets a data object for the specified key in the key-value store.
- [func set([String : Any]?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-9vmlm.md)
  Sets a dictionary object for the specified key in the key-value store.
- [func set(Double, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-1xml0.md)
  Sets a double value for the specified key in the key-value store.
- [func set(Int64, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-7tt20.md)
  Sets a `long long` value for the specified key in the key-value store.
- [func set(Any?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-9e3de.md)
  Sets an object for the specified key in the key-value store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-2rlp)*