# url(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the URL associated with the specified key.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func url(forKey defaultName: String) -> URL?
```

#### Return Value

The URL associated with `defaultName`, or `nil` if the key isn’t present in the defaults database.

#### Discussion

This method uses the data for the specified key to create and return a URL type. If the key is present but the method can’t use it to create a URL, this method returns `nil`. If a file URL contains a tilde (~) character in its path, this method replaces the tilde with an expanded path. If you saved a bookmark URL for the key previously, use the [`URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:`](nsurl/urlbyresolvingbookmarkdata:options:relativetourl:bookmarkdataisstale:error:.md) method to resolve the bookmark data and retrieve an equivalent file URL.

## Parameters

- `defaultName`: The key to retrieve from the defaults database.

## See Also

- [func bool(forKey: String) -> Bool](userdefaults/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func integer(forKey: String) -> Int](userdefaults/integer(forkey:).md)
  Returns the integer value associated with the specified key.
- [func float(forKey: String) -> Float](userdefaults/float(forkey:).md)
  Returns the floating-point value associated with the specified key.
- [func double(forKey: String) -> Double](userdefaults/double(forkey:).md)
  Returns the double value associated with the specified key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/url(forkey:))*