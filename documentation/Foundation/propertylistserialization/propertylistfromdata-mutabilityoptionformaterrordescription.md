# propertyListFromData(_:mutabilityOption:format:errorDescription:)

**Framework**: Foundation  
**Kind**: method

This method is deprecated. Use [`data(fromPropertyList:format:options:)`](propertylistserialization/data(frompropertylist:format:options:).md) instead.

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
class func propertyListFromData(_ data: Data, mutabilityOption opt: PropertyListSerialization.MutabilityOptions = [], format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?, errorDescription errorString: UnsafeMutablePointer<NSString?>?) -> Any?
```

#### Return Value

A property list object corresponding to the representation in `data`. If data is not in a supported format, returns `nil`.

## Parameters

- `data`: A data object containing a serialized property list.
- `opt`: The options used to create the property list. For possible values, see  .
- `format`: If the property list is valid, upon return contains the format.   can be  , in which case the property list format is not returned. For possible values, see  .
- `errorString`: Upon return, if the conversion is successful,   is  . If the conversion fails, upon return contains a string describing the nature of the error.

## See Also

- [class func propertyList(from: Data, options: PropertyListSerialization.ReadOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any](propertylistserialization/propertylist(from:options:format:).md)
  Creates and returns a property list from the specified data.
- [class func dataFromPropertyList(Any, format: PropertyListSerialization.PropertyListFormat, errorDescription: UnsafeMutablePointer<NSString?>?) -> Data?](propertylistserialization/datafrompropertylist(_:format:errordescription:).md)
  This method is obsolete and will be deprecated soon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistfromdata(_:mutabilityoption:format:errordescription:))*