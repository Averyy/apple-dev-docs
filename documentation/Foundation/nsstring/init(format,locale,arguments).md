# init(format:locale:arguments:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithFormat:(NSString *) format locale:(id) locale arguments:(va_list) argList;
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

See [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i) for more information.

## Parameters

- `format`: A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for examples of how to use this method, and [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265) for a list of format specifiers. This value must not be `nil`.

  > ❗ **Important**:  Raises an `NSInvalidArgumentException` if `format` is `nil`.
- `locale`: An [`NSLocale`](../nslocale.md) object specifying the locale to use. To use the current locale (specified by user preferences), pass [[`NSLocale`](../nslocale.md) [`current`](../nslocale/current.md)]. To use the system locale, pass `nil`.

  For legacy support, this may be an instance of `NSDictionary` containing locale information.
- `argList`: A list of arguments to substitute into `format`.

## See Also

### Creating and Initializing Strings
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
- [convenience init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [convenience init?(data: Data, encoding: UInt)](./init%28data,encoding%29.md)
  Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [class func localizedUserNotificationString(forKey: String, arguments: [Any]?) -> String](./localizedusernotificationstring%28forkey,arguments%29.md)
  Returns a localized string intended for display in a notification alert.
- [class func localizedStringWithFormat(NSString, any CVarArg...) -> Self](./localizedstringwithformat%28_,_%29.md)
- [typealias unichar](../unichar.md)
  Type for UTF-16 code units.
- [+ string](./string.md)
  Returns an empty string.
- [- initWithFormat:](./initwithformat_.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [- initWithFormat:locale:](./initwithformat_locale_.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale.
- [+ stringWithFormat:](./stringwithformat_.md)
  Returns a string created by using a given format string as a template into which the remaining argument values are substituted.
- [+ localizedStringWithFormat:](./localizedstringwithformat_.md)
  Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the current locale.
- [+ stringWithCharacters:length:](./stringwithcharacters_length_.md)
  Returns a string containing a given number of characters taken from a given C array of UTF-16 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(format:locale:arguments:))*