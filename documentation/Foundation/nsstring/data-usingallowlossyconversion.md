# data(using:allowLossyConversion:)

**Framework**: Foundation  
**Kind**: method

Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.

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
func data(using encoding: UInt, allowLossyConversion lossy: Bool) -> Data?
```

#### Return Value

An `NSData` object containing a representation of the receiver encoded using `encoding`. Returns `nil` if `flag` is [`false`](https://developer.apple.com/documentation/Swift/false) and the receiver can’t be converted without losing some information (such as accents or case).

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true) and the receiver can’t be converted without losing some information, some characters may be removed or altered in conversion. For example, in converting a character from `NSUnicodeStringEncoding` to `NSASCIIStringEncoding`, the character ‘Á’ becomes ‘A’, losing the accent.

This method creates an external representation (with a byte order marker, if necessary, to indicate endianness) to ensure that the resulting `NSData` object can be written out to a file safely. The result of this method, when lossless conversion is made, is the default “plain text” format for encoding and is the recommended way to save or transmit a string object.

## Parameters

- `encoding`: A string encoding. For possible values, see  .
- `lossy`: If  , then allows characters to be removed or altered in conversion.

## See Also

- [class var availableStringEncodings: UnsafePointer<UInt>](nsstring/availablestringencodings.md)
  Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [class var defaultCStringEncoding: UInt](nsstring/defaultcstringencoding.md)
  Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [class func stringEncoding(for: Data, encodingOptions: [StringEncodingDetectionOptionsKey : Any]?, convertedString: AutoreleasingUnsafeMutablePointer<NSString?>?, usedLossyConversion: UnsafeMutablePointer<ObjCBool>?) -> UInt](nsstring/stringencoding(for:encodingoptions:convertedstring:usedlossyconversion:).md)
  Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [class func localizedName(of: UInt) -> String](nsstring/localizedname(of:).md)
  Returns a human-readable string giving the name of a given encoding.
- [func canBeConverted(to: UInt) -> Bool](nsstring/canbeconverted(to:).md)
  Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [func data(using: UInt) -> Data?](nsstring/data(using:).md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [var description: String](nsstring/description.md)
- [var fastestEncoding: UInt](nsstring/fastestencoding.md)
  The fastest encoding to which the receiver may be converted without loss of information.
- [var smallestEncoding: UInt](nsstring/smallestencoding.md)
  The smallest encoding to which the receiver can be converted without loss of information.
- [struct StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](nsstring-handling-exception-names.md)
  These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/data(using:allowlossyconversion:))*