# NSAttributeDescription.AttributeType

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

The types of attributes that Core Data supports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
struct AttributeType
```

## Overview

Core Data attribute types explicitly distinguish between bit size. This allows their values to exist independent of the persistent store that contains them. A scalar option is available for a number of attribute types, in some cases by default.

| **Attribute type** | **Type** | **Scalar type** | **Scalar by default** |
| --- | --- | --- | --- |
| Integer 16 | [`NSNumber`](../../Foundation/nsnumber.md) | [`Int16`](../../Swift/int16.md) | Yes |
| Integer 32 | [`NSNumber`](../../Foundation/nsnumber.md) | [`Int32`](../../Swift/int32.md) | Yes |
| Integer 64 | [`NSNumber`](../../Foundation/nsnumber.md) | [`Int64`](../../Swift/int64.md) | Yes |
| Double | [`NSNumber`](../../Foundation/nsnumber.md) | [`Double`](../../Swift/double.md) | Yes |
| Float | [`NSNumber`](../../Foundation/nsnumber.md) | [`Float`](../../Swift/float.md) | Yes |
| Boolean | [`NSNumber`](../../Foundation/nsnumber.md) | [`Bool`](../../Swift/bool.md) | Yes |
| Date | [`NSDate`](../../Foundation/nsdate.md) | [`TimeInterval`](../../Foundation/timeinterval.md) | No |
| Decimal | [`NSDecimalNumber`](../../Foundation/nsdecimalnumber.md) | [`NSDecimalNumber`](../../Foundation/nsdecimalnumber.md) | No |
| UUID | [`UUID`](../../Foundation/uuid.md) | [`UUID`](../../Foundation/uuid.md) | No |
| URI | [`URL`](../../Foundation/url.md) | — | — |
| String | [`String`](../../Swift/string.md) | — | — |
| Binary data | [`Data`](../../Foundation/data.md) | — | — |
| Transformable | [`NSObject`](../../ObjectiveC/nsobject-swift.class.md) | — | — |
| Composite | — | — | — |
| Undefined | — | — | — |

> **Note**:  If your application uses BLOBs (binary large objects), such as image and sound files, you can choose to store their data in a location that’s external to the persistent store.

## Topics

### Attribute Types
- [static let binaryData: NSAttributeDescription.AttributeType](./attributetype-swift.struct/binarydata.md)
  An attribute that stores binary data.
- [static let boolean: NSAttributeDescription.AttributeType](./attributetype-swift.struct/boolean.md)
  An attribute that stores a Boolean value.
- [static let composite: NSAttributeDescription.AttributeType](./attributetype-swift.struct/composite.md)
  An attribute that derives its value by composing other attributes.
- [static let date: NSAttributeDescription.AttributeType](./attributetype-swift.struct/date.md)
  An attribute that stores a date.
- [static let decimal: NSAttributeDescription.AttributeType](./attributetype-swift.struct/decimal.md)
  An attribute that stores a decimal value.
- [static let double: NSAttributeDescription.AttributeType](./attributetype-swift.struct/double.md)
  An attribute that stores a double value.
- [static let float: NSAttributeDescription.AttributeType](./attributetype-swift.struct/float.md)
  An attribute that stores a float value.
- [static let integer16: NSAttributeDescription.AttributeType](./attributetype-swift.struct/integer16.md)
  An attribute that stores a 16-bit signed integer value.
- [static let integer32: NSAttributeDescription.AttributeType](./attributetype-swift.struct/integer32.md)
  An attribute that stores a 32-bit signed integer value.
- [static let integer64: NSAttributeDescription.AttributeType](./attributetype-swift.struct/integer64.md)
  An attribute that stores a 64-bit signed integer value.
- [static let objectID: NSAttributeDescription.AttributeType](./attributetype-swift.struct/objectid.md)
  An attribute that stores a managed object’s ID.
- [static let string: NSAttributeDescription.AttributeType](./attributetype-swift.struct/string.md)
  An attribute that stores a string.
- [static let transformable: NSAttributeDescription.AttributeType](./attributetype-swift.struct/transformable.md)
  An attribute that uses a value transformer to derive its value.
- [static let undefined: NSAttributeDescription.AttributeType](./attributetype-swift.struct/undefined.md)
  An attribute that doesn’t have an explicit type.
- [static let uri: NSAttributeDescription.AttributeType](./attributetype-swift.struct/uri.md)
  An attribute that stores a uniform resource identifier.
- [static let uuid: NSAttributeDescription.AttributeType](./attributetype-swift.struct/uuid.md)
  An attribute that stores a universally unique identifier.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Managing the type
- [var attributeValueClassName: String?](./attributevalueclassname.md)
  The class name that represents the attribute’s value.
- [var type: NSAttributeDescription.AttributeType](./type.md)
  The attribute’s type.
- [var attributeType: NSAttributeType](./attributetype-swift.property.md)
  The attribute’s type.
- [enum NSAttributeType](../nsattributetype.md)
  The types of attribute that Core Data supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.struct)*