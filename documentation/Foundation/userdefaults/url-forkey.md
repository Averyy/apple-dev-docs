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

The URL associated with the specified key. If the key doesn’t exist, this method returns `nil`.

#### Discussion

This method retrieves the URL associated with a key with the following behavior:

1. If the value for the key is an [`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object, the data object is used as the argument to [`unarchiveObject(with:)`](nsunarchiver/unarchiveobject(with:).md). If the data object can be unarchived as an [`NSURL`](nsurl.md), the URL is returned. If the URL can’t be archived as an [`NSURL`](nsurl.md), `nil` is returned.
2. If the value for this key is a file reference URL, the file reference URL is created, but its bookmark data isn’t resolved until the [`NSURL`](nsurl.md) object is later used (for example, with [`init(contentsOfURL:)`](nsdata/init(contentsofurl:)-6rrnr.md)).
3. If the value for the key is a string which begins with a tilde (~), the string is expanded using the [`expandingTildeInPath`](nsstring/expandingtildeinpath.md) method, from which an [`NSURL`](nsurl.md) with the `file:` scheme is created.

## Parameters

- `defaultName`: A key in the current user’s defaults database.

## See Also

- [func set(URL?, forKey: String)](userdefaults/set(_:forkey:)-2bqjt.md)
  Sets the value of the specified default key to the specified URL.
- [func object(forKey: String) -> Any?](userdefaults/object(forkey:).md)
  Returns the object associated with the specified key.
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
- [func dictionaryRepresentation() -> [String : Any]](userdefaults/dictionaryrepresentation.md)
  Returns a dictionary that contains a union of all key-value pairs in the domains in the search list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/url(forkey:))*