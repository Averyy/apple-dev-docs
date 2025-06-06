# NSAttributeDescription

**Framework**: Core Data  
**Kind**: class

A description of a single attribute belonging to an entity.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSAttributeDescription
```

#### Overview

`NSAttributeDescription` inherits from [`NSPropertyDescription`](nspropertydescription.md), which provides most of the basic behavior. Instances of `NSAttributeDescription` are used to describe attributes, as distinct from relationships. The class adds the ability to specify the attribute type, and to specify a default value. In a managed object model, you must specify the type of all attributes—you can only use the undefined attribute type (`NSUndefinedAttributeType`) for transient attributes.

##### Editing Attribute Descriptions

Attribute descriptions are editable until they are used by an object graph manager. This allows you to create or modify them dynamically. However, once a description is used (when the managed object model to which it belongs is associated with a persistent store coordinator), it  (indeed cannot) be changed. This is enforced at runtime: any attempt to mutate a model or any of its sub-objects after the model is associated with a persistent store coordinator causes an exception to be thrown. If you need to modify a model that is in use, create a copy, modify the copy, and then discard the objects with the old model.

> **Note**:  Default values set for attributes are retained by a managed object model, not copied. This means that attribute values do not have to implement the `NSCopying` protocol, however it also means that you should not modify any objects after they have been set as default values.

 Default values set for attributes are retained by a managed object model, not copied. This means that attribute values do not have to implement the `NSCopying` protocol, however it also means that you should not modify any objects after they have been set as default values.

## Topics

### Managing the type
- [var attributeValueClassName: String?](nsattributedescription/attributevalueclassname.md)
  The class name that represents the attribute’s value.
- [var type: NSAttributeDescription.AttributeType](nsattributedescription/type.md)
  The attribute’s type.
- [NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct.md)
  The types of attributes that Core Data supports.
- [var attributeType: NSAttributeType](nsattributedescription/attributetype-swift.property.md)
  The attribute’s type.
- [enum NSAttributeType](nsattributetype.md)
  The types of attribute that Core Data supports.
### Configuring the behavior
- [var allowsCloudEncryption: Bool](nsattributedescription/allowscloudencryption.md)
  A Boolean value that determines whether to encrypt the attribute’s value.
- [var allowsExternalBinaryDataStorage: Bool](nsattributedescription/allowsexternalbinarydatastorage.md)
  A Boolean value that indicates whether the attribute allows external binary storage.
- [var defaultValue: Any?](nsattributedescription/defaultvalue.md)
  The default value of the attribute.
- [var preservesValueInHistoryOnDeletion: Bool](nsattributedescription/preservesvalueinhistoryondeletion.md)
  A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.
- [var valueTransformerName: String?](nsattributedescription/valuetransformername.md)
  The name of the transformer to use for the attribute value.
### Getting version information
- [var versionHash: Data](nsattributedescription/versionhash.md)
  The version hash for the attribute.
### Deprecated
- [Deprecated symbols](nsattributedescription-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSPropertyDescription](nspropertydescription.md)
### Inherited By
- [NSCompositeAttributeDescription](nscompositeattributedescription.md)
- [NSDerivedAttributeDescription](nsderivedattributedescription.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPropertyDescription](nspropertydescription.md)
  A description of a single property belonging to an entity.
- [enum NSAttributeType](nsattributetype.md)
  The types of attribute that Core Data supports.
- [class NSRelationshipDescription](nsrelationshipdescription.md)
  A description of a relationship between two entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription)*