# defaultCStringEncoding

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns the C-string encoding assumed for any method accepting a C string as an argument.

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
class var defaultCStringEncoding: UInt { get }
```

```objc
@property (class, readonly) NSStringEncoding defaultCStringEncoding;
```

## Return Value

The C-string encoding assumed for any method accepting a C string as an argument.

## Discussion

This method returns a user-dependent encoding who value is derived from user’s default language and potentially other factors. You might sometimes need to use this encoding when interpreting user documents with unknown encodings, in the absence of other hints, but in general this encoding should be used rarely, if at all. Note that some potential values might result in unexpected encoding conversions of even fairly straightforward `NSString` content—for example, punctuation characters with a bidirectional encoding.

Methods that accept a C string as an argument use `...CString...` in the keywords for such arguments: for example, [`string(withCString:)`](./string%28withcstring%29.md)—note, though, that these are deprecated. The default C-string encoding is determined from system information and can’t be changed programmatically for an individual process. See [`NSStringEncoding`](../nsstringencoding.md) for a full list of supported encodings.

## See Also

### Working with Encodings
- [class var availableStringEncodings: UnsafePointer<UInt>](./availablestringencodings.md)
  Returns a zero-terminated list of the encodings string objects support in the application’s environment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/defaultcstringencoding)*