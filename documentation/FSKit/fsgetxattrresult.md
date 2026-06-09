# FSGetXattrResult

**Framework**: FSKit  
**Kind**: class

The result of a get-extended-attributes call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSGetXattrResult
```

#### Overview

Use this type in your implementation [`getXattr(named:of:context:replyHandler:)`](fsvolume/xattrhandler/getxattr(named:of:context:replyhandler:).md)

## Topics

### Creating a get-extended-attributes result
- [init?(xattrValue: Data)](fsgetxattrresult/init(xattrvalue:).md)
  Creates a result for an extended-attribute-getting operation.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func getXattr(named: FSFileName, of: FSItem, context: FSContext, replyHandler: (FSGetXattrResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/getxattr(named:of:context:replyhandler:).md)
  Gets the specified extended attribute of the given item.
- [func listXattrs(of: FSItem, context: FSContext, replyHandler: (FSListXattrsResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/listxattrs(of:context:replyhandler:).md)
  Gets the list of extended attributes currently set on the given item.
- [class FSListXattrsResult](fslistxattrsresult.md)
  The result of a list-extended-attributes call.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, context: FSContext, replyHandler: (FSSetXattrResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/setxattr(named:to:on:policy:context:replyhandler:).md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [class FSSetXattrResult](fssetxattrresult.md)
  The result of a set-extended-attributes call.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattrhandler/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsgetxattrresult)*