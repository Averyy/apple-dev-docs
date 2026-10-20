# url(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSURL *) URLForKey:(NSString *) defaultName;
```

#### Return Value

The URL associated with `defaultName`, or `nil` if the key isn’t present in the defaults database.

#### Discussion

This method uses the data for the specified key to create and return a URL type. If the key is present but the method can’t use it to create a URL, this method returns `nil`. If a file URL contains a tilde (~) character in its path, this method replaces the tilde with an expanded path. If you saved a bookmark URL for the key previously, use the [`URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:`](../nsurl/urlbyresolvingbookmarkdata_options_relativetourl_bookmarkdataisstale_error_.md) method to resolve the bookmark data and retrieve an equivalent file URL.

## Parameters

- `defaultName`: The key to retrieve from the defaults database.

## See Also

### Getting the value of a key
- [func bool(forKey: String) -> Bool](./bool%28forkey%29.md)
  Returns the Boolean value associated with the specified key.
- [func integer(forKey: String) -> Int](./integer%28forkey%29.md)
  Returns the integer value associated with the specified key.
- [func float(forKey: String) -> Float](./float%28forkey%29.md)
  Returns the floating-point value associated with the specified key.
- [func double(forKey: String) -> Double](./double%28forkey%29.md)
  Returns the double value associated with the specified key.
- [func string(forKey: String) -> String?](./string%28forkey%29.md)
  Returns the string associated with the specified key.
- [func stringArray(forKey: String) -> [String]?](./stringarray%28forkey%29.md)
  Returns the array of strings associated with the specified key.
- [func data(forKey: String) -> Data?](./data%28forkey%29.md)
  Returns the data object associated with the specified key.
- [func object(forKey: String) -> Any?](./object%28forkey%29.md)
  Returns the object associated with the specified key.
- [func array(forKey: String) -> [Any]?](./array%28forkey%29.md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](./dictionary%28forkey%29.md)
  Returns the dictionary object associated with the specified key.
- [func dictionaryRepresentation() -> [String : Any]](./dictionaryrepresentation%28%29.md)
  Returns a dictionary with the union of all key-value pairs found from all domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/url(forkey:))*