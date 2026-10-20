# FSItem.GetAttributesRequest

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A request to get attributes from an item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class GetAttributesRequest
```

```objc
@interface FSItemGetAttributesRequest : NSObject
```

#### Overview

Methods that retrieve attributes use this type and inspect the [`wantedAttributes`](./getattributesrequest/wantedattributes.md) property to determine which attributes to provide. FSKit calls the [`isAttributeWanted(_:)`](./getattributesrequest/isattributewanted%28_%29.md) method to determine whether the request requires a given attribute.

## Topics

### Inspecting requested attributes
- [var wantedAttributes: FSItem.Attribute](./getattributesrequest/wantedattributes.md)
  The attributes requested by the request.
- [func isAttributeWanted(FSItem.Attribute) -> Bool](./getattributesrequest/isattributewanted%28_%29.md)
  A method that indicates whether the request wants given attribute.
- [FSItem.Attribute](./attribute.md)
  A value that indicates a set of item attributes to get or set.
### Initializers
- [init?(coder: NSCoder)](./getattributesrequest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
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
- [FSItem.SetAttributesRequest](./setattributesrequest.md)
  A request to set attributes on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/getattributesrequest)*