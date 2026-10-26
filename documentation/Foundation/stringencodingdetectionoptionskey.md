# StringEncodingDetectionOptionsKey

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
struct StringEncodingDetectionOptionsKey
```

```c
typedef NSString * NSStringEncodingDetectionOptionsKey;
```

## Topics

### Type Properties
- [static let allowLossyKey: StringEncodingDetectionOptionsKey](./stringencodingdetectionoptionskey/allowlossykey.md)
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](./stringencodingdetectionoptionskey/disallowedencodingskey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](./stringencodingdetectionoptionskey/fromwindowskey.md)
- [static let likelyLanguageKey: StringEncodingDetectionOptionsKey](./stringencodingdetectionoptionskey/likelylanguagekey.md)
- [static let lossySubstitutionKey: StringEncodingDetectionOptionsKey](./stringencodingdetectionoptionskey/lossysubstitutionkey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](./stringencodingdetectionoptionskey/suggestedencodingskey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](./stringencodingdetectionoptionskey/useonlysuggestedencodingskey.md)
### Initializers
- [init(rawValue: String)](./stringencodingdetectionoptionskey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [NSString Handling Exception Names](./nsstring-handling-exception-names.md)
  These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.
- [NSStringEncoding](./nsstringencoding.md)
  The following constants are provided by `NSString` as possible string encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey)*