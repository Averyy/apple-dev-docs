# FSItem.SetAttributesRequest

**Framework**: FSKit  
**Kind**: class

A request to set attributes on an item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class SetAttributesRequest
```

#### Overview

Methods that take attributes use this type to receive attribute values and to indicate which attributes they support. The various members of the parent type, [`FSItem.Attributes`](fsitem/attributes.md), contain the values of the attributes to set.

Modify the [`consumedAttributes`](fsitem/setattributesrequest/consumedattributes.md) property to indicate which attributes your file system successfully used. FSKit calls the [`wasAttributeConsumed(_:)`](fsitem/setattributesrequest/wasattributeconsumed(_:).md) method to determine whether the file system successfully used a given attribute. Only set the attributes that your file system supports.

## Topics

### Inspecting used attributes
- [var consumedAttributes: FSItem.Attribute](fsitem/setattributesrequest/consumedattributes.md)
  The attributes successfully used by the file system.
- [func wasAttributeConsumed(FSItem.Attribute) -> Bool](fsitem/setattributesrequest/wasattributeconsumed(_:).md)
  A method that indicates whether the file system used the given attribute.
- [FSItem.Attribute](fsitem/attribute.md)
  A value that indicates a set of item attributes to get or set.

## Relationships

### Inherits From
- [FSItem.Attributes](fsitem/attributes.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/setattributesrequest)*