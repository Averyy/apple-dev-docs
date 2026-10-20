# propertyListFromData(_:mutabilityOption:format:errorDescription:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

This method is deprecated. Use [`data(fromPropertyList:format:options:)`](./data%28frompropertylist,format,options%29.md) instead.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`propertyList(from:options:format:)`](./propertylist%28from,options,format%29.md) instead.

## Declaration

```swift
class func propertyListFromData(_ data: Data, mutabilityOption opt: PropertyListSerialization.MutabilityOptions = [], format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?, errorDescription errorString: UnsafeMutablePointer<NSString?>?) -> Any?
```

```objc
+ (id) propertyListFromData:(NSData *) data mutabilityOption:(NSPropertyListMutabilityOptions) opt format:(NSPropertyListFormat *) format errorDescription:(NSString **) errorString;
```

#### Return Value

A property list object corresponding to the representation in `data`. If data is not in a supported format, returns `nil`.

## Parameters

- `data`: A data object containing a serialized property list.
- `opt`: The options used to create the property list. For possible values, see [`PropertyListSerialization.MutabilityOptions`](./mutabilityoptions.md).
- `format`: If the property list is valid, upon return contains the format. `format` can be `nil`, in which case the property list format is not returned. For possible values, see [`PropertyListSerialization.PropertyListFormat`](./propertylistformat.md).
- `errorString`: Upon return, if the conversion is successful, `errorString` is `nil`. If the conversion fails, upon return contains a string describing the nature of the error.

## See Also

### Related Documentation
- [class func propertyList(from: Data, options: PropertyListSerialization.ReadOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any](./propertylist%28from,options,format%29.md)
  Creates and returns a property list from the specified data.
### Obsolete Methods
- [class func dataFromPropertyList(Any, format: PropertyListSerialization.PropertyListFormat, errorDescription: UnsafeMutablePointer<NSString?>?) -> Data?](./datafrompropertylist%28_,format,errordescription%29.md)
  This method is obsolete and will be deprecated soon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistfromdata(_:mutabilityoption:format:errordescription:))*