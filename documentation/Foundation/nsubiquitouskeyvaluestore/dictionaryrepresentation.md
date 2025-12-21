# dictionaryRepresentation

**Framework**: Foundation  
**Kind**: property

A dictionary with all of the key-value pairs in the iCloud key-value store.

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
var dictionaryRepresentation: [String : Any] { get }
```

#### Discussion

Getting this property retrieves the in-memory copy of the keys and values. If changes to the keys and values are pending, the system fetches those changes from iCloud and updates the dictionary before returning it. To ensure the dictionary contains all recent changes, call [`synchronize()`](nsubiquitouskeyvaluestore/synchronize().md) shortly before accessing this property. All of the values in the dictionary are property list object types.

## See Also

- [func bool(forKey: String) -> Bool](nsubiquitouskeyvaluestore/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func double(forKey: String) -> Double](nsubiquitouskeyvaluestore/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func longLong(forKey: String) -> Int64](nsubiquitouskeyvaluestore/longlong(forkey:).md)
  Returns the 64-bit integer value associated with the specified key.
- [func string(forKey: String) -> String?](nsubiquitouskeyvaluestore/string(forkey:).md)
  Returns the string associated with the specified key.
- [func data(forKey: String) -> Data?](nsubiquitouskeyvaluestore/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func object(forKey: String) -> Any?](nsubiquitouskeyvaluestore/object(forkey:).md)
  Returns the object associated with the specified key.
- [func array(forKey: String) -> [Any]?](nsubiquitouskeyvaluestore/array(forkey:).md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](nsubiquitouskeyvaluestore/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/dictionaryrepresentation)*