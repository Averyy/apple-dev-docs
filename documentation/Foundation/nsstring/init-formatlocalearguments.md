# init(format:locale:arguments:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.

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
convenience init(format: String, locale: Any?, arguments argList: CVaListPointer)
```

#### Return Value

An `NSString` object initialized by using `format` as a template into which values in `argList` are substituted according the locale information in `locale`. The returned object may be different from the original receiver.

#### Discussion

The following Objective-C code fragment illustrates how to create a string from `myArgs`, which is derived from a string object with the value “Cost:” and an int with the value 32:

```objc
va_list myArgs;
 
NSString *myString = [[NSString alloc] initWithFormat:@"%@: %d\n"
                                               locale:[NSLocale currentLocale]
                                            arguments:myArgs];
```

The resulting string has the value “`Cost: 32\n`”.

See [`String Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i) for more information.

## Parameters

- `format`: A format string. See   for examples of how to use this method, and   for a list of format specifiers. This value must not be  .
- `locale`: For legacy support, this may be an instance of   containing locale information.
- `argList`: A list of arguments to substitute into  .

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
- [convenience init?(data: Data, encoding: UInt)](nsstring/init(data:encoding:).md)
  Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [class func localizedUserNotificationString(forKey: String, arguments: [Any]?) -> String](nsstring/localizedusernotificationstring(forkey:arguments:).md)
  Returns a localized string intended for display in a notification alert.
- [class func localizedStringWithFormat(NSString, any CVarArg...) -> Self](nsstring/localizedstringwithformat(_:_:).md)
- [convenience init?(CString: UnsafePointer<CChar>, encoding: UInt)](nsstring/init(cstring:encoding:)-7auq8.md)
  Returns a string containing the bytes in a given C array, interpreted according to a given encoding.
- [convenience init?(UTF8String: UnsafePointer<CChar>)](nsstring/init(utf8string:)-8bcy8.md)
  Returns a string created by copying the data from a given C array of UTF8-encoded bytes.
- [typealias unichar](unichar.md)
  Type for UTF-16 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(format:locale:arguments:))*