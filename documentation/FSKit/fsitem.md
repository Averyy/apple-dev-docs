# FSItem

**Framework**: FSKit  
**Kind**: class

A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSItem
```

#### Overview

An `FSItem` is a mostly opaque object, which your file system implementation defines as needed.

The [`FSItem.Attributes`](fsitem/attributes.md) class defines nonatomic properties to support `FSItem` instances. An [`FSItem.Attributes`](fsitem/attributes.md) instance contains a snapshot of the attributes of an `FSItem` at one point in time. The [`FSItem.Attributes`](fsitem/attributes.md) properties have no explicit thread safety provisions, since the operations that either get or set these properties enforce thread safety.

You test an attribute’s validity with the the method [`isValid(_:)`](fsitem/attributes/isvalid(_:).md). If the value is `true` (Swift) or `YES` (Objective-C), it’s safe to use the attribute.

Methods that get or set an item’s attribute use [`FSItem.GetAttributesRequest`](fsitem/getattributesrequest.md) or [`FSItem.SetAttributesRequest`](fsitem/setattributesrequest.md), respectively. Both are subclasses of [`FSItem.Attributes`](fsitem/attributes.md). An [`FSItem.GetAttributesRequest`](fsitem/getattributesrequest.md) contains a [`wantedAttributes`](fsitem/getattributesrequest/wantedattributes.md) property to indicate the attributes a file system provides for the request. Similarly, [`FSItem.SetAttributesRequest`](fsitem/setattributesrequest.md) uses the property [`consumedAttributes`](fsitem/setattributesrequest/consumedattributes.md) for a file system to signal back which attributes it successfully used.

`FSItem` is the FSKit equivelant of a vnode in the kernel. For every FSKit vnode in the kernel, the `FSModule` hosting the volume has an instantiated `FSItem`.

## Topics

### Identifying an item
- [FSItem.Identifier](fsitem/identifier.md)
- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
### Working with attributes
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem)*