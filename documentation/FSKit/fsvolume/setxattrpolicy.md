# FSVolume.SetXattrPolicy

**Framework**: FSKit  
**Kind**: enum

Flags to specify the policy when setting extended file attributes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum SetXattrPolicy
```

## Topics

### Declaring a policy
- [FSVolume.SetXattrPolicy.alwaysSet](fsvolume/setxattrpolicy/alwaysset.md)
  Set the value, regardless of previous state.
- [FSVolume.SetXattrPolicy.mustCreate](fsvolume/setxattrpolicy/mustcreate.md)
  Set the value, but fail if the extended attribute already exists.
- [FSVolume.SetXattrPolicy.mustReplace](fsvolume/setxattrpolicy/mustreplace.md)
  Set the value, but fail if the extended attribute doesn’t already exist.
- [FSVolume.SetXattrPolicy.delete](fsvolume/setxattrpolicy/delete.md)
  Delete the value, failing if the extended attribute doesn’t exist.
### Initializers
- [init?(rawValue: UInt)](fsvolume/setxattrpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func getXattr(named: FSFileName, of: FSItem, context: FSContext, replyHandler: (FSGetXattrResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/getxattr(named:of:context:replyhandler:).md)
  Gets the specified extended attribute of the given item.
- [class FSGetXattrResult](fsgetxattrresult.md)
  The result of a get-extended-attributes call.
- [func listXattrs(of: FSItem, context: FSContext, replyHandler: (FSListXattrsResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/listxattrs(of:context:replyhandler:).md)
  Gets the list of extended attributes currently set on the given item.
- [class FSListXattrsResult](fslistxattrsresult.md)
  The result of a list-extended-attributes call.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, context: FSContext, replyHandler: (FSSetXattrResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/setxattr(named:to:on:policy:context:replyhandler:).md)
  Sets the specified extended attribute data on the given item.
- [class FSSetXattrResult](fssetxattrresult.md)
  The result of a set-extended-attributes call.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattrhandler/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/setxattrpolicy)*