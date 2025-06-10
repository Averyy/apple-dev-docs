# stringEncoding(for:encodingOptions:convertedString:usedLossyConversion:)

**Framework**: Foundation  
**Kind**: method

Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func stringEncoding(for data: Data, encodingOptions opts: [StringEncodingDetectionOptionsKey : Any]? = nil, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>?, usedLossyConversion: UnsafeMutablePointer<ObjCBool>?) -> UInt
```

#### Return Value

An `NSStringEncoding` value, or `0` if a string encoding could not be determined.

## Parameters

- `data`: An   object containing bytes in an encoding to be determined.
- `opts`: Options to use when attempting to determine the string encoding. See   for a full list of supported options.
- `string`: If a string encoding could be determined, upon return contains an   object constructed from data using the determined string encoding.
- `usedLossyConversion`: If a string encoding could be determined, upon return contains a   value corresponding to whether lossy conversion was used.

## See Also

- [class var availableStringEncodings: UnsafePointer<UInt>](nsstring/availablestringencodings.md)
  Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [class var defaultCStringEncoding: UInt](nsstring/defaultcstringencoding.md)
  Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [class func localizedName(of: UInt) -> String](nsstring/localizedname(of:).md)
  Returns a human-readable string giving the name of a given encoding.
- [func canBeConverted(to: UInt) -> Bool](nsstring/canbeconverted(to:).md)
  Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [func data(using: UInt) -> Data?](nsstring/data(using:).md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [func data(using: UInt, allowLossyConversion: Bool) -> Data?](nsstring/data(using:allowlossyconversion:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/stringencoding(for:encodingoptions:convertedstring:usedlossyconversion:))*