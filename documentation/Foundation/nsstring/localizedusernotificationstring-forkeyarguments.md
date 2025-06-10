# localizedUserNotificationString(forKey:arguments:)

**Framework**: Foundation  
**Kind**: method

Returns a localized string intended for display in a notification alert.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func localizedUserNotificationString(forKey key: String, arguments: [Any]?) -> String
```

#### Return Value

A string whose value is created dynamically from a localized string resource. If a string resource corresponding to the specified `key` cannot be found, the returned string is empty.

#### Discussion

When configuring the content of a local notification using the User Notifications framework, use this method to create strings whose contents are stored in your app’s `Localizable.strings` file. When the notification is about to be displayed, the string object uses the key and arguments you specify to load the appropriate localized version of the string. If the localized string has any escaped character sequences—that is, special characters proceeded by a percent (%) sign—those character sequences are replaced by the values in the `arguments` parameter.

For information about how strings are formatted, see [`String Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6) in [`Resource Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i).

## Parameters

- `key`: The key to use when looking up the string in the app’s   file.
- `arguments`: An array of values to substitute for escaped characters in the string.

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
- [class func localizedStringWithFormat(NSString, any CVarArg...) -> Self](nsstring/localizedstringwithformat(_:_:).md)
- [convenience init?(CString: UnsafePointer<CChar>, encoding: UInt)](nsstring/init(cstring:encoding:)-7auq8.md)
  Returns a string containing the bytes in a given C array, interpreted according to a given encoding.
- [convenience init?(UTF8String: UnsafePointer<CChar>)](nsstring/init(utf8string:)-8bcy8.md)
  Returns a string created by copying the data from a given C array of UTF8-encoded bytes.
- [typealias unichar](unichar.md)
  Type for UTF-16 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/localizedusernotificationstring(forkey:arguments:))*