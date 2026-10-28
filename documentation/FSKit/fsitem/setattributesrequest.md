# FSItem.SetAttributesRequest

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A request to set attributes on an item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class SetAttributesRequest
```

```objc
@interface FSItemSetAttributesRequest : FSItemAttributes
```

## Overview

Methods that take attributes use this type to receive attribute values and to indicate which attributes they support. The various members of the parent type, [`FSItem.Attributes`](./attributes.md), contain the values of the attributes to set.

Modify the [`consumedAttributes`](./setattributesrequest/consumedattributes.md) property to indicate which attributes your file system successfully used. FSKit calls the [`wasAttributeConsumed(_:)`](./setattributesrequest/wasattributeconsumed%28_%29.md) method to determine whether the file system successfully used a given attribute. Only set the attributes that your file system supports.

## Topics

### Inspecting used attributes
- [var consumedAttributes: FSItem.Attribute](./setattributesrequest/consumedattributes.md)
  The attributes successfully used by the file system.
- [func wasAttributeConsumed(FSItem.Attribute) -> Bool](./setattributesrequest/wasattributeconsumed%28_%29.md)
  A method that indicates whether the file system used the given attribute.
- [FSItem.Attribute](./attribute.md)
  A value that indicates a set of item attributes to get or set.

## Relationships

### Inherits From
- [FSItem.Attributes](./attributes.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Working with attributes
- [FSItem.Attributes](./attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [FSItem.GetAttributesRequest](./getattributesrequest.md)
  A request to get attributes from an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/setattributesrequest)*