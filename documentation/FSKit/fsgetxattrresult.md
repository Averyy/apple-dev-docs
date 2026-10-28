# FSGetXattrResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a get-extended-attributes call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSGetXattrResult
```

```objc
@interface FSGetXattrResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation [`getXattr(named:of:context:replyHandler:)`](./fsvolume/xattrhandler/getxattr%28named,of,context,replyhandler%29.md)

## Topics

### Creating a get-extended-attributes result
- [init?(xattrValue: Data)](./fsgetxattrresult/init%28xattrvalue%29.md)
  Creates a result for an extended-attribute-getting operation.

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

### Reading and writing
- [func getXattr(named: FSFileName, of: FSItem, context: FSContext, replyHandler: (FSGetXattrResult?, (any Error)?) -> Void)](./fsvolume/xattrhandler/getxattr%28named,of,context,replyhandler%29.md)
  Gets the specified extended attribute of the given item.
- [func listXattrs(of: FSItem, context: FSContext, replyHandler: (FSListXattrsResult?, (any Error)?) -> Void)](./fsvolume/xattrhandler/listxattrs%28of,context,replyhandler%29.md)
  Gets the list of extended attributes currently set on the given item.
- [class FSListXattrsResult](./fslistxattrsresult.md)
  The result of a list-extended-attributes call.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, context: FSContext, replyHandler: (FSSetXattrResult?, (any Error)?) -> Void)](./fsvolume/xattrhandler/setxattr%28named,to,on,policy,context,replyhandler%29.md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](./fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [class FSSetXattrResult](./fssetxattrresult.md)
  The result of a set-extended-attributes call.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](./fsvolume/xattrhandler/supportedxattrnames%28for%29.md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsgetxattrresult)*