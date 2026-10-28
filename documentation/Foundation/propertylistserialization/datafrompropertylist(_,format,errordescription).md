# dataFromPropertyList(_:format:errorDescription:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

This method is obsolete and will be deprecated soon.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`data(fromPropertyList:format:options:)`](./data%28frompropertylist,format,options%29.md) instead.

## Declaration

```swift
class func dataFromPropertyList(_ plist: Any, format: PropertyListSerialization.PropertyListFormat, errorDescription errorString: UnsafeMutablePointer<NSString?>?) -> Data?
```

```objc
+ (NSData *) dataFromPropertyList:(id) plist format:(NSPropertyListFormat) format errorDescription:(NSString **) errorString;
```

## Return Value

An `NSData` object containing `plist` in the format specified by `format`.

## Discussion

This method is obsolete and will be deprecated soon. Use [`data(fromPropertyList:format:options:)`](./data%28frompropertylist,format,options%29.md) instead.

## Parameters

- `plist`: A property list object.
- `format`: A property list format. For possible values, see [`PropertyListSerialization.PropertyListFormat`](./propertylistformat.md).
- `errorString`: Upon return, if the conversion is successful, `errorString` is `nil`. If the conversion fails, upon return contains a string describing the nature of the error.

## See Also

### Related Documentation
- [class func data(fromPropertyList: Any, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions) throws -> Data](./data%28frompropertylist,format,options%29.md)
  Returns an `NSData` object containing a given property list in a specified format.
### Obsolete Methods
- [class func propertyListFromData(Data, mutabilityOption: PropertyListSerialization.MutabilityOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?, errorDescription: UnsafeMutablePointer<NSString?>?) -> Any?](./propertylistfromdata%28_,mutabilityoption,format,errordescription%29.md)
  This method is deprecated. Use [`data(fromPropertyList:format:options:)`](./data%28frompropertylist,format,options%29.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/datafrompropertylist(_:format:errordescription:))*