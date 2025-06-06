# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets the value of the specified default key to the specified URL.

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
func set(_ url: URL?, forKey defaultName: String)
```

#### Discussion

If `url` is a file URL, this method takes the [`absoluteURL`](nsurl/absoluteurl.md), determines whether its path can be made relative to the user’s home directory, and if so, abbreviates it using the [`abbreviatingWithTildeInPath`](nsstring/abbreviatingwithtildeinpath.md) method.

If `url` isn’t a file URL, a data object is created by calling the [`archivedData(withRootObject:)`](nskeyedarchiver/archiveddata(withrootobject:).md) method and passing `url` as the root object.

## Parameters

- `url`: The URL to store in the defaults database.
- `defaultName`: The key with which to associate the value.

## See Also

- [func url(forKey: String) -> URL?](userdefaults/url(forkey:).md)
  Returns the URL associated with the specified key.
- [func set(Any?, forKey: String)](userdefaults/set(_:forkey:)-8ab6d.md)
  Sets the value of the specified default key.
- [func set(Float, forKey: String)](userdefaults/set(_:forkey:)-1t5ec.md)
  Sets the value of the specified default key to the specified float value.
- [func set(Double, forKey: String)](userdefaults/set(_:forkey:)-2w22f.md)
  Sets the value of the specified default key to the double value.
- [func set(Int, forKey: String)](userdefaults/set(_:forkey:)-3v852.md)
  Sets the value of the specified default key to the specified integer value.
- [func set(Bool, forKey: String)](userdefaults/set(_:forkey:)-3nn5m.md)
  Sets the value of the specified default key to the specified Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-2bqjt)*