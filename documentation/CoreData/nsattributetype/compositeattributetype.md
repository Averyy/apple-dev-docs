# NSAttributeType.compositeAttributeType

**Framework**: Core Data  
**Kind**: case

An attribute that derives its value by composing other attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case compositeAttributeType
```

#### Discussion

Composite attributes support all attribute types except the following:

- [`NSAttributeType.undefinedAttributeType`](nsattributetype/undefinedattributetype.md)
- [`NSAttributeType.objectIDAttributeType`](nsattributetype/objectidattributetype.md)
- [`NSAttributeType.binaryDataAttributeType`](nsattributetype/binarydataattributetype.md) (when [`allowsExternalBinaryDataStorage`](nsattributedescription/allowsexternalbinarydatastorage.md) is [`true`](https://developer.apple.com/documentation/Swift/true))

For more information, see [`NSCompositeAttributeDescription`](nscompositeattributedescription.md).

## See Also

- [NSAttributeType.binaryDataAttributeType](nsattributetype/binarydataattributetype.md)
  An attribute that stores binary data.
- [NSAttributeType.booleanAttributeType](nsattributetype/booleanattributetype.md)
  An attribute that stores a Boolean value.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributetype/compositeattributetype)*