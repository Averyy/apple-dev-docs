# FSListXattrsResult

**Framework**: FSKit  
**Kind**: class

The result of a list-extended-attributes call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSListXattrsResult
```

#### Overview

Use this type in your implementation of [`supportedXattrNames(for:)`](fsvolume/xattrhandler/supportedxattrnames(for:).md).

## Topics

### Creating a list-extended-attributes result
- [init?(xattrNames: [FSFileName])](fslistxattrsresult/init(xattrnames:).md)
  Creates a result instance with all required properties populated.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.

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
- [class FSGetXattrResult](fsgetxattrresult.md)
  The result of a get-extended-attributes call.
- [func listXattrs(of: FSItem, context: FSContext, replyHandler: (FSListXattrsResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/listxattrs(of:context:replyhandler:).md)
  Gets the list of extended attributes currently set on the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, context: FSContext, replyHandler: (FSSetXattrResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/setxattr(named:to:on:policy:context:replyhandler:).md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [class FSSetXattrResult](fssetxattrresult.md)
  The result of a set-extended-attributes call.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattrhandler/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fslistxattrsresult)*