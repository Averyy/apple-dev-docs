# PropertyListSerialization

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that converts between a property list and one of several serialized representations.

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
class PropertyListSerialization
```

```objc
@interface NSPropertyListSerialization : NSObject
```

## Overview

The [`PropertyListSerialization`](./propertylistserialization.md) class provides methods that convert a property list to and from several serialized formats. A property list is itself an array or dictionary that contains only [`NSData`](./nsdata.md), [`NSString`](./nsstring.md), [`NSArray`](./nsarray.md), [`NSDictionary`](./nsdictionary.md), [`NSDate`](./nsdate.md), and [`NSNumber`](./nsnumber.md) objects.

Property list objects are toll-free bridged with their respective Core Foundation types ([`CFData`](../CoreFoundation/cfdata.md), [`CFString`](../CoreFoundation/cfstring.md), and so on). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2)  for more information on toll-free bridging.

## Topics

### Serializing a Property List
- [class func data(fromPropertyList: Any, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions) throws -> Data](./propertylistserialization/data%28frompropertylist,format,options%29.md)
  Returns an `NSData` object containing a given property list in a specified format.
- [class func writePropertyList(Any, to: OutputStream, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions, error: NSErrorPointer) -> Int](./propertylistserialization/writepropertylist%28_,to,format,options,error%29.md)
  Writes a property list to the specified stream.
- [PropertyListSerialization.WriteOptions](./propertylistserialization/writeoptions.md)
### Deserializing a Property List
- [class func propertyList(from: Data, options: PropertyListSerialization.ReadOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any](./propertylistserialization/propertylist%28from,options,format%29.md)
  Creates and returns a property list from the specified data.
- [class func propertyList(with: InputStream, options: PropertyListSerialization.ReadOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any](./propertylistserialization/propertylist%28with,options,format%29.md)
  Creates and returns a property list by reading from the specified stream.
### Validating a Property List
- [class func propertyList(Any, isValidFor: PropertyListSerialization.PropertyListFormat) -> Bool](./propertylistserialization/propertylist%28_,isvalidfor%29.md)
  Returns a Boolean value that indicates whether a given property list is valid for a given format.
### Obsolete Methods
- [class func dataFromPropertyList(Any, format: PropertyListSerialization.PropertyListFormat, errorDescription: UnsafeMutablePointer<NSString?>?) -> Data?](./propertylistserialization/datafrompropertylist%28_,format,errordescription%29.md)
  This method is obsolete and will be deprecated soon.
- [class func propertyListFromData(Data, mutabilityOption: PropertyListSerialization.MutabilityOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?, errorDescription: UnsafeMutablePointer<NSString?>?) -> Any?](./propertylistserialization/propertylistfromdata%28_,mutabilityoption,format,errordescription%29.md)
  This method is deprecated. Use [`data(fromPropertyList:format:options:)`](./propertylistserialization/data%28frompropertylist,format,options%29.md) instead.
### Constants
- [PropertyListSerialization.MutabilityOptions](./propertylistserialization/mutabilityoptions.md)
  These constants specify mutability options in property lists.
- [PropertyListSerialization.PropertyListFormat](./propertylistserialization/propertylistformat.md)
  These constants are used to specify a property list serialization format.
- [PropertyListSerialization.ReadOptions](./propertylistserialization/readoptions.md)
  The only read options supported are described in [`PropertyListSerialization.MutabilityOptions`](./propertylistserialization/mutabilityoptions.md).
### Error Codes
- [var NSPropertyListReadCorruptError: Int](./nspropertylistreadcorrupterror-swift.var.md)
  Parsing of the property list failed.
- [var NSPropertyListReadUnknownVersionError: Int](./nspropertylistreadunknownversionerror-swift.var.md)
  The version number of the property list cannot be determined.
- [var NSPropertyListReadStreamError: Int](./nspropertylistreadstreamerror-swift.var.md)
  Reading of the property list failed.
- [var NSPropertyListWriteStreamError: Int](./nspropertylistwritestreamerror-swift.var.md)
  Writing to the property list failed.
- [var NSPropertyListWriteInvalidError: Int](./nspropertylistwriteinvaliderror-swift.var.md)
  Writing failed because of an invalid property list object, or an invalid property list type was specified.
- [var NSPropertyListErrorMinimum: Int](./nspropertylisterrorminimum-swift.var.md)
  The start of the range of error codes reserved for property list errors.
- [var NSPropertyListErrorMaximum: Int](./nspropertylisterrormaximum-swift.var.md)
  The end of the range of error codes reserved for property list errors.
- [NSPropertyListReadCorruptError](./nspropertylistreadcorrupterror-c.enum.case.md)
  Parsing of the property list failed.
- [NSPropertyListReadUnknownVersionError](./nspropertylistreadunknownversionerror-c.enum.case.md)
  The version number of the property list cannot be determined.
- [NSPropertyListReadStreamError](./nspropertylistreadstreamerror-c.enum.case.md)
  Reading of the property list failed.
- [NSPropertyListWriteStreamError](./nspropertylistwritestreamerror-c.enum.case.md)
  Writing to the property list failed.
- [NSPropertyListWriteInvalidError](./nspropertylistwriteinvaliderror-c.enum.case.md)
  Writing failed because of an invalid property list object, or an invalid property list type was specified.
- [NSPropertyListErrorMinimum](./nspropertylisterrorminimum-c.enum.case.md)
  The start of the range of error codes reserved for property list errors.
- [NSPropertyListErrorMaximum](./nspropertylisterrormaximum-c.enum.case.md)
  The end of the range of error codes reserved for property list errors.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Property Lists
- [class PropertyListEncoder](./propertylistencoder.md)
  An object that encodes instances of data types to a property list.
- [class PropertyListDecoder](./propertylistdecoder.md)
  An object that decodes instances of data types from a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization)*