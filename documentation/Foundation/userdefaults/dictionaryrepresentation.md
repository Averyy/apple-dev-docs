# dictionaryRepresentation()

**Framework**: Foundation  
**Kind**: method

Returns a dictionary with the union of all key-value pairs found from all domains.

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
func dictionaryRepresentation() -> [String : Any]
```

#### Return Value

A dictionary with the combined set of keys and values from all domains.

#### Discussion

Use this method to retrieve a union of the keys and values available to your app. The dictionary contains the data from all of the available domains. If multiple domains contain a value for the same key, the dictionary includes the value from the earliest occurrence of that key and discards the values in subsequent domains.

The values in the dictionary are one of the property list object types, such as [`NSNumber`](NSNumber.md), [`NSString`](NSString.md), [`Data`](data.md), [`Date`](date.md), [`NSArray`](NSArray.md), or [`NSDictionary`](NSDictionary.md).

## See Also

- [func bool(forKey: String) -> Bool](userdefaults/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func integer(forKey: String) -> Int](userdefaults/integer(forkey:).md)
  Returns the integer value associated with the specified key.
- [func float(forKey: String) -> Float](userdefaults/float(forkey:).md)
  Returns the floating-point value associated with the specified key.
- [func double(forKey: String) -> Double](userdefaults/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func url(forKey: String) -> URL?](userdefaults/url(forkey:).md)
  Returns the URL associated with the specified key.
- [func string(forKey: String) -> String?](userdefaults/string(forkey:).md)
  Returns the string associated with the specified key.
- [func stringArray(forKey: String) -> [String]?](userdefaults/stringarray(forkey:).md)
  Returns the array of strings associated with the specified key.
- [func data(forKey: String) -> Data?](userdefaults/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func object(forKey: String) -> Any?](userdefaults/object(forkey:).md)
  Returns the object associated with the specified key.
- [func array(forKey: String) -> [Any]?](userdefaults/array(forkey:).md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](userdefaults/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/dictionaryrepresentation())*