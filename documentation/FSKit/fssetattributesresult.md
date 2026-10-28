# FSSetAttributesResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The restlt of a set-attributes call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSSetAttributesResult
```

```objc
@interface FSSetAttributesResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation of [`setAttributes(_:on:context:replyHandler:)`](./fsvolume/handler/setattributes%28_,on,context,replyhandler%29.md).

## Topics

### Creating a set-attributes result
- [init?(attributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](./fssetattributesresult/init%28attributes,freespace%29.md)
  Creates a result for an attribute-setting operation.
- [FSItem.Attributes](./fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](./fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with attributes
- [func getAttributes(FSItem.GetAttributesRequest, of: FSItem, context: FSContext, replyHandler: (FSGetAttributesResult?, (any Error)?) -> Void)](./fsvolume/handler/getattributes%28_,of,context,replyhandler%29.md)
  Fetches attributes for the given item.
- [FSItem.GetAttributesRequest](./fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [class FSGetAttributesResult](./fsgetattributesresult.md)
  The result of a get-attributes call.
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, context: FSContext, replyHandler: (FSSetAttributesResult?, (any Error)?) -> Void)](./fsvolume/handler/setattributes%28_,on,context,replyhandler%29.md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](./fsitem/setattributesrequest.md)
  A request to set attributes on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fssetattributesresult)*