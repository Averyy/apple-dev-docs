# NSStringEncoding

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

The following constants are provided by `NSString` as possible string encodings.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
typedef NSUInteger NSStringEncoding;
```

#### Discussion

These values represent the various character encodings supported by the `NSString` classes. This is an incomplete list. Additional encodings are defined in [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i) (see `CFStringEncodingExt.h`); these encodings can be used with `NSString` by first passing the Core Foundation encoding to the [`CFStringConvertEncodingToNSStringEncoding(_:)`](../CoreFoundation/cfstringconvertencodingtonsstringencoding%28_%29.md) function.

## Topics

### Constants
- [var NSASCIIStringEncoding: UInt](./nsasciistringencoding.md)
  Strict 7-bit ASCII encoding within 8-bit chars; ASCII values 0…127 only.
- [var NSNEXTSTEPStringEncoding: UInt](./nsnextstepstringencoding.md)
  8-bit ASCII encoding with NEXTSTEP extensions.
- [var NSJapaneseEUCStringEncoding: UInt](./nsjapaneseeucstringencoding.md)
  8-bit EUC encoding for Japanese text.
- [var NSUTF8StringEncoding: UInt](./nsutf8stringencoding.md)
  An 8-bit representation of Unicode characters, suitable for transmission or storage by ASCII-based systems.
- [var NSISOLatin1StringEncoding: UInt](./nsisolatin1stringencoding.md)
  8-bit ISO Latin 1 encoding.
- [var NSSymbolStringEncoding: UInt](./nssymbolstringencoding.md)
  8-bit Adobe Symbol encoding vector.
- [var NSNonLossyASCIIStringEncoding: UInt](./nsnonlossyasciistringencoding.md)
  7-bit verbose ASCII to represent all Unicode characters.
- [var NSShiftJISStringEncoding: UInt](./nsshiftjisstringencoding.md)
  8-bit Shift-JIS encoding for Japanese text.
- [var NSISOLatin2StringEncoding: UInt](./nsisolatin2stringencoding.md)
  8-bit ISO Latin 2 encoding.
- [var NSUnicodeStringEncoding: UInt](./nsunicodestringencoding.md)
  The canonical Unicode encoding for string objects.
- [var NSWindowsCP1251StringEncoding: UInt](./nswindowscp1251stringencoding.md)
  Microsoft Windows codepage 1251, encoding Cyrillic characters; equivalent to AdobeStandardCyrillic font encoding.
- [var NSWindowsCP1252StringEncoding: UInt](./nswindowscp1252stringencoding.md)
  Microsoft Windows codepage 1252; equivalent to WinLatin1.
- [var NSWindowsCP1253StringEncoding: UInt](./nswindowscp1253stringencoding.md)
  Microsoft Windows codepage 1253, encoding Greek characters.
- [var NSWindowsCP1254StringEncoding: UInt](./nswindowscp1254stringencoding.md)
  Microsoft Windows codepage 1254, encoding Turkish characters.
- [var NSWindowsCP1250StringEncoding: UInt](./nswindowscp1250stringencoding.md)
  Microsoft Windows codepage 1250; equivalent to WinLatin2.
- [var NSISO2022JPStringEncoding: UInt](./nsiso2022jpstringencoding.md)
  ISO 2022 Japanese encoding for email.
- [var NSMacOSRomanStringEncoding: UInt](./nsmacosromanstringencoding.md)
  Classic Macintosh Roman encoding.
- [var NSUTF16StringEncoding: UInt](./nsutf16stringencoding.md)
- [var NSUTF16BigEndianStringEncoding: UInt](./nsutf16bigendianstringencoding.md)
  `NSUTF16StringEncoding` encoding with explicit endianness specified.
- [var NSUTF16LittleEndianStringEncoding: UInt](./nsutf16littleendianstringencoding.md)
  `NSUTF16StringEncoding` encoding with explicit endianness specified.
- [var NSUTF32StringEncoding: UInt](./nsutf32stringencoding.md)
  32-bit UTF encoding.
- [var NSUTF32BigEndianStringEncoding: UInt](./nsutf32bigendianstringencoding.md)
  `NSUTF32StringEncoding` encoding with explicit endianness specified.
- [var NSUTF32LittleEndianStringEncoding: UInt](./nsutf32littleendianstringencoding.md)
  `NSUTF32StringEncoding` encoding with explicit endianness specified.
- [var NSProprietaryStringEncoding: UInt](./nsproprietarystringencoding.md)
  Installation-specific encoding.

## See Also

### Working with Encodings
- [class var availableStringEncodings: UnsafePointer<UInt>](./nsstring/availablestringencodings.md)
  Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [class var defaultCStringEncoding: UInt](./nsstring/defaultcstringencoding.md)
  Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [class func stringEncoding(for: Data, encodingOptions: [StringEncodingDetectionOptionsKey : Any]?, convertedString: AutoreleasingUnsafeMutablePointer<NSString?>?, usedLossyConversion: UnsafeMutablePointer<ObjCBool>?) -> UInt](./nsstring/stringencoding%28for,encodingoptions,convertedstring,usedlossyconversion%29.md)
  Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [class func localizedName(of: UInt) -> String](./nsstring/localizedname%28of%29.md)
  Returns a human-readable string giving the name of a given encoding.
- [func canBeConverted(to: UInt) -> Bool](./nsstring/canbeconverted%28to%29.md)
  Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [func data(using: UInt) -> Data?](./nsstring/data%28using%29.md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [func data(using: UInt, allowLossyConversion: Bool) -> Data?](./nsstring/data%28using,allowlossyconversion%29.md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [var description: String](./nsstring/description.md)
- [var fastestEncoding: UInt](./nsstring/fastestencoding.md)
  The fastest encoding to which the receiver may be converted without loss of information.
- [var smallestEncoding: UInt](./nsstring/smallestencoding.md)
  The smallest encoding to which the receiver can be converted without loss of information.
- [struct StringEncodingDetectionOptionsKey](./stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](./nsstring-handling-exception-names.md)
  These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringencoding)*