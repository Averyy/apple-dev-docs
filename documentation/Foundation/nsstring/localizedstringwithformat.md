# localizedStringWithFormat(_:_:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func localizedStringWithFormat(_ format: NSString, _ args: any CVarArg...) -> Self
```

## See Also

- [init()](nsstring/init.md)
  Returns an initialized `NSString` object that contains no characters.
- [convenience init?(bytes: UnsafeRawPointer, length: Int, encoding: UInt)](nsstring/init(bytes:length:encoding:).md)
  Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [convenience init?(bytesNoCopy: UnsafeMutableRawPointer, length: Int, encoding: UInt, freeWhenDone: Bool)](nsstring/init(bytesnocopy:length:encoding:freewhendone:).md)
  Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [convenience init(characters: UnsafePointer<unichar>, length: Int)](nsstring/init(characters:length:).md)
  Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [convenience init(charactersNoCopy: UnsafeMutablePointer<unichar>, length: Int, freeWhenDone: Bool)](nsstring/init(charactersnocopy:length:freewhendone:).md)
  Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [convenience init(string: String)](nsstring/init(string:)-210xa.md)
  Returns an `NSString` object initialized by copying the characters from another given string.
- [convenience init?(CString: UnsafePointer<CChar>, encoding: UInt)](nsstring/init(cstring:encoding:)-20f9h.md)
  Returns an `NSString` object initialized using the characters in a given C array, interpreted according to a given encoding.
- [convenience init?(UTF8String: UnsafePointer<CChar>)](nsstring/init(utf8string:)-vg2b.md)
  Returns an `NSString` object initialized by copying the characters from a given C array of UTF8-encoded bytes.
- [convenience init(format: String, arguments: CVaListPointer)](nsstring/init(format:arguments:).md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [convenience init(format: String, locale: Any?, arguments: CVaListPointer)](nsstring/init(format:locale:arguments:).md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [convenience init?(data: Data, encoding: UInt)](nsstring/init(data:encoding:).md)
  Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [class func localizedUserNotificationString(forKey: String, arguments: [Any]?) -> String](nsstring/localizedusernotificationstring(forkey:arguments:).md)
  Returns a localized string intended for display in a notification alert.
- [convenience init?(CString: UnsafePointer<CChar>, encoding: UInt)](nsstring/init(cstring:encoding:)-7auq8.md)
  Returns a string containing the bytes in a given C array, interpreted according to a given encoding.
- [convenience init?(UTF8String: UnsafePointer<CChar>)](nsstring/init(utf8string:)-8bcy8.md)
  Returns a string created by copying the data from a given C array of UTF8-encoded bytes.
- [typealias unichar](unichar.md)
  Type for UTF-16 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/localizedstringwithformat(_:_:))*