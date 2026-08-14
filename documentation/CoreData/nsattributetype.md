# NSAttributeType

**Framework**: Core Data  
**Kind**: enum

The types of attribute that Core Data supports.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum NSAttributeType
```

## Mentions

- [Configuring Attributes](configuring-attributes.md)

#### Overview

Core Data supports the following attribute types, which differentiate between bit sizes to enable data-store independence. For some types, a scalar option is available.

| **Attribute Type** | **Type** | **Scalar type** | **Scalar by default?** |
| --- | --- | --- | --- |
| Integer 16 | [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) | [`int16_t`](https://developer.apple.com/documentation/kernel/int16_t) | yes |
| Integer 32 | [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) | [`int32_t`](https://developer.apple.com/documentation/kernel/int32_t) | yes |
| Integer 64 | [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) | [`int64_t`](https://developer.apple.com/documentation/kernel/int64_t) | yes |
| Double | [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) | `double` | yes |
| Float | [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) | `float` | yes |
| Boolean | [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) | [`BOOL`](https://developer.apple.com/documentation/objectivec/bool) | yes |
| Date | [`NSDate`](https://developer.apple.com/documentation/foundation/nsdate) | [`TimeInterval`](https://developer.apple.com/documentation/foundation/timeinterval) | no |
| Decimal | [`NSDecimalNumber`](https://developer.apple.com/documentation/foundation/nsdecimalnumber) | [`NSDecimalNumber`](https://developer.apple.com/documentation/foundation/nsdecimalnumber) | no |
| UUID | [`NSUUID`](https://developer.apple.com/documentation/foundation/nsuuid) | [`NSUUID`](https://developer.apple.com/documentation/foundation/nsuuid) | no |
| URI | [`NSURL`](https://developer.apple.com/documentation/foundation/nsurl) | — | — |
| String | [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) | — | — |
| Binary data | [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) | — | — |
| Transformable | [`NSObject`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class) | — | — |
| Composite | — | — | — |
| Undefined | — | — | — |

> **Note**:  If your application uses Binary Large Objects (BLOBs) like image and sound data, prefer to store its binary data outside of the Core Data store.

## Topics

### Attribute types
- [NSAttributeType.binaryDataAttributeType](nsattributetype/binarydataattributetype.md)
  An attribute that stores binary data.
- [NSAttributeType.booleanAttributeType](nsattributetype/booleanattributetype.md)
  An attribute that stores a Boolean value.
- [NSAttributeType.compositeAttributeType](nsattributetype/compositeattributetype.md)
  An attribute that derives its value by composing other attributes.
- [NSAttributeType.dateAttributeType](nsattributetype/dateattributetype.md)
  An attribute that stores a date.
- [NSAttributeType.decimalAttributeType](nsattributetype/decimalattributetype.md)
  An attribute that stores a decimal value.
- [NSAttributeType.doubleAttributeType](nsattributetype/doubleattributetype.md)
  An attribute that stores a double value.
- [NSAttributeType.floatAttributeType](nsattributetype/floatattributetype.md)
  An attribute that stores a float value.
- [NSAttributeType.integer16AttributeType](nsattributetype/integer16attributetype.md)
  An attribute that stores a 16-bit signed integer value.
- [NSAttributeType.integer32AttributeType](nsattributetype/integer32attributetype.md)
  An attribute that stores a 32-bit signed integer value.
- [NSAttributeType.integer64AttributeType](nsattributetype/integer64attributetype.md)
  An attribute that stores a 64-bit signed integer value.
- [NSAttributeType.objectIDAttributeType](nsattributetype/objectidattributetype.md)
  An attribute that stores a managed object’s ID.
- [NSAttributeType.stringAttributeType](nsattributetype/stringattributetype.md)
  An attribute that stores a string.
- [NSAttributeType.transformableAttributeType](nsattributetype/transformableattributetype.md)
  An attribute that uses a value transformer to derive its value.
- [NSAttributeType.undefinedAttributeType](nsattributetype/undefinedattributetype.md)
  An attribute that doesn’t have an explicit type.
- [NSAttributeType.URIAttributeType](nsattributetype/uriattributetype.md)
  An attribute that stores a uniform resource identifier.
- [NSAttributeType.UUIDAttributeType](nsattributetype/uuidattributetype.md)
  An attribute that stores a universally unique identifier.
### Initializers
- [init?(rawValue: UInt)](nsattributetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class NSPropertyDescription](nspropertydescription.md)
  A description of a single property belonging to an entity.
- [class NSAttributeDescription](nsattributedescription.md)
  A description of a single attribute belonging to an entity.
- [class NSRelationshipDescription](nsrelationshipdescription.md)
  A description of a relationship between two entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributetype)*