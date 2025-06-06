# bool(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the Boolean value associated with the specified key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func bool(forKey defaultName: String) -> Bool
```

#### Return Value

The Boolean value associated with the specified key. If the specified key doesn’t exist, this method returns [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method automatically coerces certain “truthy” values—such as the strings “true”, “YES”, and “1”, and the numbers 1 and 1.0—to the Boolean value [`true`](https://developer.apple.com/documentation/swift/true). The same is true for certain “falsy” values—such as the strings “false”, “NO”, and “0”, and the numbers 0 and 0.0—which are automatically coerced to the Boolean value [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `defaultName`: A key in the current user’s defaults database.

## See Also

- [func set(Bool, forKey: String)](userdefaults/set(_:forkey:)-3nn5m.md)
  Sets the value of the specified default key to the specified Boolean value.
- [func object(forKey: String) -> Any?](userdefaults/object(forkey:).md)
  Returns the object associated with the specified key.
- [func url(forKey: String) -> URL?](userdefaults/url(forkey:).md)
  Returns the URL associated with the specified key.
- [func array(forKey: String) -> [Any]?](userdefaults/array(forkey:).md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](userdefaults/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.
- [func string(forKey: String) -> String?](userdefaults/string(forkey:).md)
  Returns the string associated with the specified key.
- [func stringArray(forKey: String) -> [String]?](userdefaults/stringarray(forkey:).md)
  Returns the array of strings associated with the specified key.
- [func data(forKey: String) -> Data?](userdefaults/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func integer(forKey: String) -> Int](userdefaults/integer(forkey:).md)
  Returns the integer value associated with the specified key.
- [func float(forKey: String) -> Float](userdefaults/float(forkey:).md)
  Returns the float value associated with the specified key.
- [func double(forKey: String) -> Double](userdefaults/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func dictionaryRepresentation() -> [String : Any]](userdefaults/dictionaryrepresentation.md)
  Returns a dictionary that contains a union of all key-value pairs in the domains in the search list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/bool(forkey:))*