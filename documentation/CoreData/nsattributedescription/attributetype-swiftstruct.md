# NSAttributeDescription.AttributeType

**Framework**: Core Data  
**Kind**: struct

The types of attributes that Core Data supports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
struct AttributeType
```

#### Overview

Core Data attribute types explicitly distinguish between bit size. This allows their values to exist independent of the persistent store that contains them. A scalar option is available for a number of attribute types, in some cases by default.

|  |  |  |  |
| --- | --- | --- | --- |
| Integer 16 | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) | [`Int16`](https://developer.apple.com/documentation/Swift/Int16) | Yes |
| Integer 32 | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) | [`Int32`](https://developer.apple.com/documentation/Swift/Int32) | Yes |
| Integer 64 | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) | [`Int64`](https://developer.apple.com/documentation/Swift/Int64) | Yes |
| Double | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) | [`Double`](https://developer.apple.com/documentation/Swift/Double) | Yes |
| Float | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) | [`Float`](https://developer.apple.com/documentation/Swift/Float) | Yes |
| Boolean | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) | [`Bool`](https://developer.apple.com/documentation/Swift/Bool) | Yes |
| Date | [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) | [`TimeInterval`](https://developer.apple.com/documentation/Foundation/TimeInterval) | No |
| Decimal | [`NSDecimalNumber`](https://developer.apple.com/documentation/Foundation/NSDecimalNumber) | [`NSDecimalNumber`](https://developer.apple.com/documentation/Foundation/NSDecimalNumber) | No |
| UUID | [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) | [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) | No |
| URI | [`URL`](https://developer.apple.com/documentation/Foundation/URL) | — | — |
| String | [`String`](https://developer.apple.com/documentation/Swift/String) | — | — |
| Binary data | [`Data`](https://developer.apple.com/documentation/Foundation/Data) | — | — |
| Transformable | [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) | — | — |
| Composite | — | — | — |
| Undefined | — | — | — |

> **Note**:  If your application uses BLOBs (binary large objects), such as image and sound files, you can choose to store their data in a location that’s external to the persistent store.

## Topics

### Attribute Types
- [static let binaryData: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/binarydata.md)
  An attribute that stores binary data.
- [static let boolean: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/boolean.md)
  An attribute that stores a Boolean value.
- [static let composite: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/composite.md)
  An attribute that derives its value by composing other attributes.
- [static let date: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/date.md)
  An attribute that stores a date.
- [static let decimal: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/decimal.md)
  An attribute that stores a decimal value.
- [static let double: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/double.md)
  An attribute that stores a double value.
- [static let float: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/float.md)
  An attribute that stores a float value.
- [static let integer16: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/integer16.md)
  An attribute that stores a 16-bit signed integer value.
- [static let integer32: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/integer32.md)
  An attribute that stores a 32-bit signed integer value.
- [static let integer64: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/integer64.md)
  An attribute that stores a 64-bit signed integer value.
- [static let objectID: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/objectid.md)
  An attribute that stores a managed object’s ID.
- [static let string: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/string.md)
  An attribute that stores a string.
- [static let transformable: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/transformable.md)
  An attribute that uses a value transformer to derive its value.
- [static let undefined: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/undefined.md)
  An attribute that doesn’t have an explicit type.
- [static let uri: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/uri.md)
  An attribute that stores a uniform resource identifier.
- [static let uuid: NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct/uuid.md)
  An attribute that stores a universally unique identifier.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var attributeValueClassName: String?](nsattributedescription/attributevalueclassname.md)
  The class name that represents the attribute’s value.
- [var type: NSAttributeDescription.AttributeType](nsattributedescription/type.md)
  The attribute’s type.
- [var attributeType: NSAttributeType](nsattributedescription/attributetype-swift.property.md)
  The attribute’s type.
- [enum NSAttributeType](nsattributetype.md)
  The types of attribute that Core Data supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.struct)*