# stringWithCharacters:length:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a string containing a given number of characters taken from a given C array of UTF-16 code units.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) stringWithCharacters:(const unichar *) characters length:(NSUInteger) length;
```

## Return Value

A string containing `length` UTF-16 code units taken (starting with the first) from `chars`.

## Parameters

- `characters`: A C array of UTF-16 code units; the value must not be `NULL`.

  > ❗ **Important**:  Raises an exception if `chars` is `NULL`, even if `length` is `0`.
- `length`: The number of characters to use from `chars`.

## See Also

### Creating and Initializing Strings
- [+ string](./string.md)
  Returns an empty string.
- [init()](./init%28%29.md)
  Returns an initialized `NSString` object that contains no characters.
- [convenience init?(bytes: UnsafeRawPointer, length: Int, encoding: UInt)](./init%28bytes,length,encoding%29.md)
  Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [convenience init?(bytesNoCopy: UnsafeMutableRawPointer, length: Int, encoding: UInt, freeWhenDone: Bool)](./init%28bytesnocopy,length,encoding,freewhendone%29.md)
  Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [convenience init(characters: UnsafePointer<unichar>, length: Int)](./init%28characters,length%29.md)
  Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [convenience init(charactersNoCopy: UnsafeMutablePointer<unichar>, length: Int, freeWhenDone: Bool)](./init%28charactersnocopy,length,freewhendone%29.md)
  Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [convenience init(string: String)](./init%28string%29-210xa.md)
  Returns an `NSString` object initialized by copying the characters from another given string.
- [- initWithFormat:](./initwithformat_.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [convenience init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [- initWithFormat:locale:](./initwithformat_locale_.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale.
- [convenience init(format: String, locale: Any?, arguments: CVaListPointer)](./init%28format,locale,arguments%29.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [convenience init?(data: Data, encoding: UInt)](./init%28data,encoding%29.md)
  Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [+ stringWithFormat:](./stringwithformat_.md)
  Returns a string created by using a given format string as a template into which the remaining argument values are substituted.
- [+ localizedStringWithFormat:](./localizedstringwithformat_.md)
  Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the current locale.
- [class func localizedUserNotificationString(forKey: String, arguments: [Any]?) -> String](./localizedusernotificationstring%28forkey,arguments%29.md)
  Returns a localized string intended for display in a notification alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/stringwithcharacters:length:)*