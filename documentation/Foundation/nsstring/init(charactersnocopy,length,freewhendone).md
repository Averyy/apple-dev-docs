# init(charactersNoCopy:length:freeWhenDone:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.

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
convenience init(charactersNoCopy characters: UnsafeMutablePointer<unichar>, length: Int, freeWhenDone freeBuffer: Bool)
```

```objc
- (instancetype) initWithCharactersNoCopy:(unichar *) characters length:(NSUInteger) length freeWhenDone:(BOOL) freeBuffer;
```

## Return Value

An initialized `NSString` object that contains `length` characters from `characters`. The returned object may be different from the original receiver.

## Discussion

If an error occurs during the creation of the string, then `bytes` is not freed even if `flag` is [`true`](../../Swift/true.md). In this case, the caller is responsible for freeing the buffer. This allows the caller to continue trying to create a string with the buffer, without having the buffer deallocated.

## Parameters

- `characters`: A C array of UTF-16 code units.
- `length`: The number of characters to use from `characters`.
- `freeBuffer`: If [`true`](../../Swift/true.md), the receiver releases the memory with `free()` when it no longer needs the data; if [`false`](../../Swift/false.md) it won’t.

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
- [convenience init(string: String)](./init%28string%29-210xa.md)
  Returns an `NSString` object initialized by copying the characters from another given string.
- [convenience init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [convenience init(format: String, locale: Any?, arguments: CVaListPointer)](./init%28format,locale,arguments%29.md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
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
### Related Documentation
- [+ stringWithCharacters:length:](./stringwithcharacters_length_.md)
  Returns a string containing a given number of characters taken from a given C array of UTF-16 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(charactersnocopy:length:freewhendone:))*