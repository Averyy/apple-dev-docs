# init(bytes:length:encoding:)

**Framework**: Foundation  
**Kind**: init

Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.

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
convenience init?(bytes: UnsafeRawPointer, length len: Int, encoding: UInt)
```

#### Return Value

An initialized `NSString` object containing `length` bytes from `bytes` interpreted using the encoding `encoding`. The returned object may be different from the original receiver. The return byte strings are allowed to be unterminated. If the length of the byte string is greater than the specified length a `nil` value is returned.

## Parameters

- `bytes`: A buffer of bytes interpreted in the encoding specified by `encoding`.
- `len`: The number of bytes to use from `bytes`.
- `encoding`: The character encoding applied to `bytes`. For possible values, see [`NSStringEncoding`](nsstringencoding.md).

## See Also

- [init()](nsstring/init.md)
  Returns an initialized `NSString` object that contains no characters.
- [convenience init?(bytesNoCopy: UnsafeMutableRawPointer, length: Int, encoding: UInt, freeWhenDone: Bool)](nsstring/init(bytesnocopy:length:encoding:freewhendone:).md)
  Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [convenience init(characters: UnsafePointer<unichar>, length: Int)](nsstring/init(characters:length:).md)
  Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [convenience init(charactersNoCopy: UnsafeMutablePointer<unichar>, length: Int, freeWhenDone: Bool)](nsstring/init(charactersnocopy:length:freewhendone:).md)
  Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [convenience init(string: String)](nsstring/init(string:)-210xa.md)
  Returns an `NSString` object initialized by copying the characters from another given string.
- [convenience init(format: String, arguments: CVaListPointer)](nsstring/init(format:arguments:).md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [convenience init(format: String, locale: Any?, arguments: CVaListPointer)](nsstring/init(format:locale:arguments:).md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [convenience init?(data: Data, encoding: UInt)](nsstring/init(data:encoding:).md)
  Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [class func localizedUserNotificationString(forKey: String, arguments: [Any]?) -> String](nsstring/localizedusernotificationstring(forkey:arguments:).md)
  Returns a localized string intended for display in a notification alert.
- [class func localizedStringWithFormat(NSString, any CVarArg...) -> Self](nsstring/localizedstringwithformat(_:_:).md)
- [typealias unichar](unichar.md)
  Type for UTF-16 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(bytes:length:encoding:))*