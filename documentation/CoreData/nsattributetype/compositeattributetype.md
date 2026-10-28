# NSAttributeType.compositeAttributeType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

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

```c
NSCompositeAttributeType
```

## Discussion

Composite attributes support all attribute types except the following:

- [`NSAttributeType.undefinedAttributeType`](./undefinedattributetype.md)
- [`NSAttributeType.objectIDAttributeType`](./objectidattributetype.md)
- [`NSAttributeType.binaryDataAttributeType`](./binarydataattributetype.md) (when [`allowsExternalBinaryDataStorage`](../nsattributedescription/allowsexternalbinarydatastorage.md) is [`true`](../../Swift/true.md))

For more information, see [`NSCompositeAttributeDescription`](../nscompositeattributedescription.md).

## See Also

### Attribute types
- [NSAttributeType.binaryDataAttributeType](./binarydataattributetype.md)
  An attribute that stores binary data.
- [NSAttributeType.booleanAttributeType](./booleanattributetype.md)
  An attribute that stores a Boolean value.
- [NSAttributeType.dateAttributeType](./dateattributetype.md)
  An attribute that stores a date.
- [NSAttributeType.decimalAttributeType](./decimalattributetype.md)
  An attribute that stores a decimal value.
- [NSAttributeType.doubleAttributeType](./doubleattributetype.md)
  An attribute that stores a double value.
- [NSAttributeType.floatAttributeType](./floatattributetype.md)
  An attribute that stores a float value.
- [NSAttributeType.integer16AttributeType](./integer16attributetype.md)
  An attribute that stores a 16-bit signed integer value.
- [NSAttributeType.integer32AttributeType](./integer32attributetype.md)
  An attribute that stores a 32-bit signed integer value.
- [NSAttributeType.integer64AttributeType](./integer64attributetype.md)
  An attribute that stores a 64-bit signed integer value.
- [NSAttributeType.objectIDAttributeType](./objectidattributetype.md)
  An attribute that stores a managed object’s ID.
- [NSAttributeType.stringAttributeType](./stringattributetype.md)
  An attribute that stores a string.
- [NSAttributeType.transformableAttributeType](./transformableattributetype.md)
  An attribute that uses a value transformer to derive its value.
- [NSAttributeType.undefinedAttributeType](./undefinedattributetype.md)
  An attribute that doesn’t have an explicit type.
- [NSAttributeType.URIAttributeType](./uriattributetype.md)
  An attribute that stores a uniform resource identifier.
- [NSAttributeType.UUIDAttributeType](./uuidattributetype.md)
  An attribute that stores a universally unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributetype/compositeattributetype)*