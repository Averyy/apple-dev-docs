# init(format:arguments:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.

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
convenience init(format: String, arguments argList: CVaListPointer)
```

#### Return Value

An `NSString` object initialized by using `format` as a template into which the values in `argList` are substituted according to the current locale. The returned object may be different from the original receiver.

#### Discussion

This method is meant to be called from within a variadic function, where the argument list will be available.

This method invokes [`init(format:locale:arguments:)`](nsstring/init(format:locale:arguments:).md) without applying any localization. This is useful, for example, when working with fixed-format representations of information that is written out and read back in at a later time.

> ❗ **Important**:  When working with text that’s presented to the user, use the [`localizedStringWithFormat:`](nsstring/localizedstringwithformat:.md) method, or the [`initWithFormat:locale:`](nsstring/initwithformat:locale:.md) or [`init(format:locale:arguments:)`](nsstring/init(format:locale:arguments:).md) method, passing [`current`](nslocale/current.md) as the locale.

## Parameters

- `format`: A format string. See [`Formatting String Objects`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for examples of how to use this method, and [`String Format Specifiers`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265) for a list of format specifiers. This value must not be `nil`. > ❗ **Important**:  Raises an `NSInvalidArgumentException` if `format` is `nil`.
- `argList`: A list of arguments to substitute into `format`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(format:arguments:))*