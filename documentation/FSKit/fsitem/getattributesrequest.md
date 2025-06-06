# FSItem.GetAttributesRequest

**Framework**: FSKit  
**Kind**: class

A request to get attributes from an item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class GetAttributesRequest
```

#### Overview

Methods that retrieve attributes use this type and inspect the [`wantedAttributes`](fsitem/getattributesrequest/wantedattributes.md) property to determine which attributes to provide. FSKit calls the [`isAttributeWanted(_:)`](fsitem/getattributesrequest/isattributewanted(_:).md) method to determine whether the request requires a given attribute.

## Topics

### Inspecting requested attributes
- [var wantedAttributes: FSItem.Attribute](fsitem/getattributesrequest/wantedattributes.md)
  The attributes requested by the request.
- [func isAttributeWanted(FSItem.Attribute) -> Bool](fsitem/getattributesrequest/isattributewanted(_:).md)
  A method that indicates whether the request wants given attribute.
- [FSItem.Attribute](fsitem/attribute.md)
  A value that indicates a set of item attributes to get or set.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/getattributesrequest)*