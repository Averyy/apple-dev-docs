# undefined

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

An attribute that doesn’t have an explicit type.

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
static let undefined: NSAttributeDescription.AttributeType
```

## Discussion

Use this attribute type with transient attributues only. Core Data manages the attribute’s value and registers the necessary undo and redo actions.

## See Also

### Attribute Types
- [static let binaryData: NSAttributeDescription.AttributeType](./binarydata.md)
  An attribute that stores binary data.
- [static let boolean: NSAttributeDescription.AttributeType](./boolean.md)
  An attribute that stores a Boolean value.
- [static let composite: NSAttributeDescription.AttributeType](./composite.md)
  An attribute that derives its value by composing other attributes.
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
- [static let uri: NSAttributeDescription.AttributeType](./uri.md)
  An attribute that stores a uniform resource identifier.
- [static let uuid: NSAttributeDescription.AttributeType](./uuid.md)
  An attribute that stores a universally unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.struct/undefined)*