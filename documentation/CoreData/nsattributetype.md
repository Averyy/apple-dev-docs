# NSAttributeType

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

The types of attribute that Core Data supports.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum NSAttributeType
```

```c
enum NSAttributeType : NSUInteger;
```

## Mentions

- [Configuring Attributes](./configuring-attributes.md)

## Overview

Core Data supports the following attribute types, which differentiate between bit sizes to enable data-store independence. For some types, a scalar option is available.

| **Attribute Type** | **Type** | **Scalar type** | **Scalar by default?** |
| --- | --- | --- | --- |
| Integer 16 | [`NSNumber`](../Foundation/nsnumber.md) | [`int16_t`](../kernel/int16_t.md) | yes |
| Integer 32 | [`NSNumber`](../Foundation/nsnumber.md) | [`int32_t`](../kernel/int32_t.md) | yes |
| Integer 64 | [`NSNumber`](../Foundation/nsnumber.md) | [`int64_t`](../kernel/int64_t.md) | yes |
| Double | [`NSNumber`](../Foundation/nsnumber.md) | `double` | yes |
| Float | [`NSNumber`](../Foundation/nsnumber.md) | `float` | yes |
| Boolean | [`NSNumber`](../Foundation/nsnumber.md) | [`BOOL`](../ObjectiveC/bool.md) | yes |
| Date | [`NSDate`](../Foundation/nsdate.md) | [`TimeInterval`](../Foundation/timeinterval.md) | no |
| Decimal | [`NSDecimalNumber`](../Foundation/nsdecimalnumber.md) | [`NSDecimalNumber`](../Foundation/nsdecimalnumber.md) | no |
| UUID | [`NSUUID`](../Foundation/nsuuid.md) | [`NSUUID`](../Foundation/nsuuid.md) | no |
| URI | [`NSURL`](../Foundation/nsurl.md) | — | — |
| String | [`NSString`](../Foundation/nsstring.md) | — | — |
| Binary data | [`NSData`](../Foundation/nsdata.md) | — | — |
| Transformable | [`NSObject`](../ObjectiveC/nsobject-swift.class.md) | — | — |
| Composite | — | — | — |
| Undefined | — | — | — |

> **Note**:  If your application uses Binary Large Objects (BLOBs) like image and sound data, prefer to store its binary data outside of the Core Data store.

## Topics

### Attribute types
- [NSAttributeType.binaryDataAttributeType](./nsattributetype/binarydataattributetype.md)
  An attribute that stores binary data.
- [NSAttributeType.booleanAttributeType](./nsattributetype/booleanattributetype.md)
  An attribute that stores a Boolean value.
- [NSAttributeType.compositeAttributeType](./nsattributetype/compositeattributetype.md)
  An attribute that derives its value by composing other attributes.
- [NSAttributeType.dateAttributeType](./nsattributetype/dateattributetype.md)
  An attribute that stores a date.
- [NSAttributeType.decimalAttributeType](./nsattributetype/decimalattributetype.md)
  An attribute that stores a decimal value.
- [NSAttributeType.doubleAttributeType](./nsattributetype/doubleattributetype.md)
  An attribute that stores a double value.
- [NSAttributeType.floatAttributeType](./nsattributetype/floatattributetype.md)
  An attribute that stores a float value.
- [NSAttributeType.integer16AttributeType](./nsattributetype/integer16attributetype.md)
  An attribute that stores a 16-bit signed integer value.
- [NSAttributeType.integer32AttributeType](./nsattributetype/integer32attributetype.md)
  An attribute that stores a 32-bit signed integer value.
- [NSAttributeType.integer64AttributeType](./nsattributetype/integer64attributetype.md)
  An attribute that stores a 64-bit signed integer value.
- [NSAttributeType.objectIDAttributeType](./nsattributetype/objectidattributetype.md)
  An attribute that stores a managed object’s ID.
- [NSAttributeType.stringAttributeType](./nsattributetype/stringattributetype.md)
  An attribute that stores a string.
- [NSAttributeType.transformableAttributeType](./nsattributetype/transformableattributetype.md)
  An attribute that uses a value transformer to derive its value.
- [NSAttributeType.undefinedAttributeType](./nsattributetype/undefinedattributetype.md)
  An attribute that doesn’t have an explicit type.
- [NSAttributeType.URIAttributeType](./nsattributetype/uriattributetype.md)
  An attribute that stores a uniform resource identifier.
- [NSAttributeType.UUIDAttributeType](./nsattributetype/uuidattributetype.md)
  An attribute that stores a universally unique identifier.
### Initializers
- [init?(rawValue: UInt)](./nsattributetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Standard attributes
- [class NSPropertyDescription](./nspropertydescription.md)
  A description of a single property belonging to an entity.
- [class NSAttributeDescription](./nsattributedescription.md)
  A description of a single attribute belonging to an entity.
- [class NSRelationshipDescription](./nsrelationshipdescription.md)
  A description of a relationship between two entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributetype)*