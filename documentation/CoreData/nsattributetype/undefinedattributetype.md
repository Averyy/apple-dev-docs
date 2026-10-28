# NSAttributeType.undefinedAttributeType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

An attribute that doesn’t have an explicit type.

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
case undefinedAttributeType
```

```c
NSUndefinedAttributeType
```

## Discussion

Use this attribute type with transient attributues only. Core Data manages the attribute’s value and registers the necessary undo and redo actions.

## See Also

### Attribute types
- [NSAttributeType.binaryDataAttributeType](./binarydataattributetype.md)
  An attribute that stores binary data.
- [NSAttributeType.booleanAttributeType](./booleanattributetype.md)
  An attribute that stores a Boolean value.
- [NSAttributeType.compositeAttributeType](./compositeattributetype.md)
  An attribute that derives its value by composing other attributes.
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
- [NSAttributeType.URIAttributeType](./uriattributetype.md)
  An attribute that stores a uniform resource identifier.
- [NSAttributeType.UUIDAttributeType](./uuidattributetype.md)
  An attribute that stores a universally unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributetype/undefinedattributetype)*