# integer(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the integer value associated with the specified key.

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
func integer(forKey defaultName: String) -> Int
```

#### Return Value

The integer value associated with `defaultName`, or `0` if the key isn’t present in the defaults database.

#### Discussion

This method automatically coerces certain types to their equivalent integer values. The Boolean value `true` becomes `1` and `false` becomes `0`. A floating-point number becomes the greatest integer that’s less than the stored number –– for example, `2.67` becomes `2`. A string that contains a numerical value contains the equivalent integer value — for example, “123” becomes `123`.

## Parameters

- `defaultName`: The key to retrieve from the defaults database.

## See Also

- [func bool(forKey: String) -> Bool](userdefaults/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
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
- [func dictionaryRepresentation() -> [String : Any]](userdefaults/dictionaryrepresentation.md)
  Returns a dictionary with the union of all key-value pairs found from all domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/integer(forkey:))*