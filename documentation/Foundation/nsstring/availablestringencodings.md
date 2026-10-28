# availableStringEncodings

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns a zero-terminated list of the encodings string objects support in the application’s environment.

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
class var availableStringEncodings: UnsafePointer<UInt> { get }
```

```objc
@property (class, readonly) const NSStringEncoding * availableStringEncodings;
```

## Return Value

A zero-terminated list of the encodings string objects support in the application’s environment.

## Discussion

Among the more commonly used encodings are:

- [`NSASCIIStringEncoding`](../nsasciistringencoding.md)
- [`NSUnicodeStringEncoding`](../nsunicodestringencoding.md)
- [`NSISOLatin1StringEncoding`](../nsisolatin1stringencoding.md)
- [`NSISOLatin2StringEncoding`](../nsisolatin2stringencoding.md)
- [`NSSymbolStringEncoding`](../nssymbolstringencoding.md)

See the [`NSStringEncoding`](../nsstringencoding.md) type for a larger list and descriptions of many supported encodings. In addition to those encodings listed here, you can also use the encodings defined for CFString in Core Foundation; you just need to call the [`CFStringConvertEncodingToNSStringEncoding(_:)`](../../CoreFoundation/cfstringconvertencodingtonsstringencoding%28_%29.md) function to convert them to a usable format.

## See Also

### Working with Encodings
- [class var defaultCStringEncoding: UInt](./defaultcstringencoding.md)
  Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [class func stringEncoding(for: Data, encodingOptions: [StringEncodingDetectionOptionsKey : Any]?, convertedString: AutoreleasingUnsafeMutablePointer<NSString?>?, usedLossyConversion: UnsafeMutablePointer<ObjCBool>?) -> UInt](./stringencoding%28for,encodingoptions,convertedstring,usedlossyconversion%29.md)
  Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [class func localizedName(of: UInt) -> String](./localizedname%28of%29.md)
  Returns a human-readable string giving the name of a given encoding.
- [func canBeConverted(to: UInt) -> Bool](./canbeconverted%28to%29.md)
  Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [func data(using: UInt) -> Data?](./data%28using%29.md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [func data(using: UInt, allowLossyConversion: Bool) -> Data?](./data%28using,allowlossyconversion%29.md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [var description: String](./description.md)
- [var fastestEncoding: UInt](./fastestencoding.md)
  The fastest encoding to which the receiver may be converted without loss of information.
- [var smallestEncoding: UInt](./smallestencoding.md)
  The smallest encoding to which the receiver can be converted without loss of information.
- [struct StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](../nsstring-handling-exception-names.md)
  These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.
- [NSStringEncoding](../nsstringencoding.md)
  The following constants are provided by `NSString` as possible string encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/availablestringencodings)*