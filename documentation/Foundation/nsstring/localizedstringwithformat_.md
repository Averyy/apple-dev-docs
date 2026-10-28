# localizedStringWithFormat:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the current locale.

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
+ (instancetype) localizedStringWithFormat:(NSString *) format;
```

## Return Value

A string created by using `format` as a template into which the following argument values are substituted according to the formatting information in the current locale.

## Discussion

Pass a comma-separated list of variadic arguments to substitute into `format`.

This method is equivalent to using [`initWithFormat:locale:`](./initwithformat_locale_.md) and passing the current locale as the locale argument.

As an example of formatting, this method replaces the decimal according to the locale in `%f` and `%d` substitutions, and calls [`description(withLocale:)`](../nsnumber/description%28withlocale%29.md) instead of [`description()`](../../ObjectiveC/nsobject-swift.class/description%28%29.md) where necessary.

This code excerpt creates a string from another string and a float:

```objc
NSString *myString = [NSString localizedStringWithFormat:@"%@:  %f\n", @"Cost", 1234.56];
```

The resulting string has the value “`Cost: 1234.560000\n`” if the locale is `en_US`, and “`Cost: 1234,560000\n`” if the locale is `fr_FR`.

See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for more information.

## Parameters

- `format`: A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for examples of how to use this method, and [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265) for a list of format specifiers. This value must not be `nil`.

  Raises an `NSInvalidArgumentException` if `format` is `nil`.

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
- [class func localizedUserNotificationString(forKey: String, arguments: [Any]?) -> String](./localizedusernotificationstring%28forkey,arguments%29.md)
  Returns a localized string intended for display in a notification alert.
- [+ stringWithCharacters:length:](./stringwithcharacters_length_.md)
  Returns a string containing a given number of characters taken from a given C array of UTF-16 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/localizedstringwithformat:)*