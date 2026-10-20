# FSGetAttributesResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a get-attributes call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSGetAttributesResult
```

```objc
@interface FSGetAttributesResult : FSVolumeHandlerResult
```

#### Overview

Use this type in your implementation of [`getAttributes(_:of:context:replyHandler:)`](./fsvolume/handler/getattributes%28_,of,context,replyhandler%29.md).

## Topics

### Creating a get-attributes result
- [init?(attributes: FSItem.Attributes)](./fsgetattributesresult/init%28attributes%29.md)
  Creates a result for an attribute-getting operation.
- [FSItem.Attributes](./fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.

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
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, context: FSContext, replyHandler: (FSSetAttributesResult?, (any Error)?) -> Void)](./fsvolume/handler/setattributes%28_,on,context,replyhandler%29.md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](./fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSSetAttributesResult](./fssetattributesresult.md)
  The restlt of a set-attributes call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsgetattributesresult)*