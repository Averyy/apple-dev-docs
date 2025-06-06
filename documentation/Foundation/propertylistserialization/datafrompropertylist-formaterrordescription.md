# dataFromPropertyList(_:format:errorDescription:)

**Framework**: Foundation  
**Kind**: method

This method is obsolete and will be deprecated soon.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func dataFromPropertyList(_ plist: Any, format: PropertyListSerialization.PropertyListFormat, errorDescription errorString: UnsafeMutablePointer<NSString?>?) -> Data?
```

#### Return Value

An `NSData` object containing `plist` in the format specified by `format`.

#### Discussion

This method is obsolete and will be deprecated soon. Use [`data(fromPropertyList:format:options:)`](propertylistserialization/data(frompropertylist:format:options:).md) instead.

## Parameters

- `plist`: A property list object.
- `format`: A property list format. For possible values, see  .
- `errorString`: Upon return, if the conversion is successful,   is  . If the conversion fails, upon return contains a string describing the nature of the error.

## See Also

- [class func data(fromPropertyList: Any, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions) throws -> Data](propertylistserialization/data(frompropertylist:format:options:).md)
  Returns an `NSData` object containing a given property list in a specified format.
- [class func propertyListFromData(Data, mutabilityOption: PropertyListSerialization.MutabilityOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?, errorDescription: UnsafeMutablePointer<NSString?>?) -> Any?](propertylistserialization/propertylistfromdata(_:mutabilityoption:format:errordescription:).md)
  This method is deprecated. Use [`data(fromPropertyList:format:options:)`](propertylistserialization/data(frompropertylist:format:options:).md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/datafrompropertylist(_:format:errordescription:))*