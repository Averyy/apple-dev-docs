# dictionaryRepresentation()

**Framework**: Foundation  
**Kind**: method

Returns a dictionary that contains a union of all key-value pairs in the domains in the search list.

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

A dictionary containing the keys. The keys are names of defaults and the value corresponding to each key is a property list object ([`NSData`](nsdata.md), [`NSString`](nsstring.md), [`NSNumber`](nsnumber.md), [`NSDate`](nsdate.md), [`NSArray`](nsarray.md), or [`NSDictionary`](nsdictionary.md)).

#### Discussion

As with [`object(forKey:)`](userdefaults/object(forkey:).md), key-value pairs in domains that are earlier in the search list take precedence. The combined result does not preserve information about which domain each entry came from.

## See Also

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
- [func bool(forKey: String) -> Bool](userdefaults/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func integer(forKey: String) -> Int](userdefaults/integer(forkey:).md)
  Returns the integer value associated with the specified key.
- [func float(forKey: String) -> Float](userdefaults/float(forkey:).md)
  Returns the float value associated with the specified key.
- [func double(forKey: String) -> Double](userdefaults/double(forkey:).md)
  Returns the double value associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/dictionaryrepresentation())*