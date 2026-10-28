# composite

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

An attribute that derives its value by composing other attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
static let composite: NSAttributeDescription.AttributeType
```

## Discussion

Composite attributes support all attribute types except the following:

- [`undefined`](./undefined.md)
- [`objectID`](./objectid.md)
- [`binaryData`](./binarydata.md) (when [`allowsExternalBinaryDataStorage`](../allowsexternalbinarydatastorage.md) is [`true`](../../../Swift/true.md))

For more information, see [`NSCompositeAttributeDescription`](../../nscompositeattributedescription.md).

## See Also

### Attribute Types
- [static let binaryData: NSAttributeDescription.AttributeType](./binarydata.md)
  An attribute that stores binary data.
- [static let boolean: NSAttributeDescription.AttributeType](./boolean.md)
  An attribute that stores a Boolean value.
- [static let date: NSAttributeDescription.AttributeType](./date.md)
  An attribute that stores a date.
- [static let decimal: NSAttributeDescription.AttributeType](./decimal.md)
  An attribute that stores a decimal value.
- [static let double: NSAttributeDescription.AttributeType](./double.md)
  An attribute that stores a double value.
- [static let float: NSAttributeDescription.AttributeType](./float.md)
  An attribute that stores a float value.
- [static let integer16: NSAttributeDescription.AttributeType](./integer16.md)
  An attribute that stores a 16-bit signed integer value.
- [static let integer32: NSAttributeDescription.AttributeType](./integer32.md)
  An attribute that stores a 32-bit signed integer value.
- [static let integer64: NSAttributeDescription.AttributeType](./integer64.md)
  An attribute that stores a 64-bit signed integer value.
- [static let objectID: NSAttributeDescription.AttributeType](./objectid.md)
  An attribute that stores a managed object’s ID.
- [static let string: NSAttributeDescription.AttributeType](./string.md)
  An attribute that stores a string.
- [static let transformable: NSAttributeDescription.AttributeType](./transformable.md)
  An attribute that uses a value transformer to derive its value.
- [static let undefined: NSAttributeDescription.AttributeType](./undefined.md)
  An attribute that doesn’t have an explicit type.
- [static let uri: NSAttributeDescription.AttributeType](./uri.md)
  An attribute that stores a uniform resource identifier.
- [static let uuid: NSAttributeDescription.AttributeType](./uuid.md)
  An attribute that stores a universally unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.struct/composite)*