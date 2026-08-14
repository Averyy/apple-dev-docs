# FSSetAttributesResult

**Framework**: FSKit  
**Kind**: class

The restlt of a set-attributes call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSSetAttributesResult
```

#### Overview

Use this type in your implementation of [`setAttributes(_:on:context:replyHandler:)`](fsvolume/handler/setattributes(_:on:context:replyhandler:).md).

## Topics

### Creating a set-attributes result
- [init?(attributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](fssetattributesresult/init(attributes:freespace:).md)
  Creates a result for an attribute-setting operation.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func getAttributes(FSItem.GetAttributesRequest, of: FSItem, context: FSContext, replyHandler: (FSGetAttributesResult?, (any Error)?) -> Void)](fsvolume/handler/getattributes(_:of:context:replyhandler:).md)
  Fetches attributes for the given item.
- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [class FSGetAttributesResult](fsgetattributesresult.md)
  The result of a get-attributes call.
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, context: FSContext, replyHandler: (FSSetAttributesResult?, (any Error)?) -> Void)](fsvolume/handler/setattributes(_:on:context:replyhandler:).md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fssetattributesresult)*