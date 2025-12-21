# string(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the string associated with the specified key.

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
func string(forKey aKey: String) -> String?
```

#### Return Value

The string associated with `aKey`, or `nil` if the key isn’t present.

#### Discussion

This method automatically coerces certain types to equivalent strings. For example, it converts the integer `123` to the string “123”. If the key is present, but the method can’t use it to create an appropriate string, this method returns `nil`.

## Parameters

- `aKey`: The key to retrieve from the iCloud key-value store.

## See Also

- [func bool(forKey: String) -> Bool](nsubiquitouskeyvaluestore/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func double(forKey: String) -> Double](nsubiquitouskeyvaluestore/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func longLong(forKey: String) -> Int64](nsubiquitouskeyvaluestore/longlong(forkey:).md)
  Returns the 64-bit integer value associated with the specified key.
- [func data(forKey: String) -> Data?](nsubiquitouskeyvaluestore/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func object(forKey: String) -> Any?](nsubiquitouskeyvaluestore/object(forkey:).md)
  Returns the object associated with the specified key.
- [func array(forKey: String) -> [Any]?](nsubiquitouskeyvaluestore/array(forkey:).md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](nsubiquitouskeyvaluestore/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.
- [var dictionaryRepresentation: [String : Any]](nsubiquitouskeyvaluestore/dictionaryrepresentation.md)
  A dictionary with all of the key-value pairs in the iCloud key-value store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/string(forkey:))*