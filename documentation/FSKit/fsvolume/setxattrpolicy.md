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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func getXattr(named: FSFileName, of: FSItem, replyHandler: (Data?, (any Error)?) -> Void)](fsvolume/xattroperations/getxattr(named:of:replyhandler:).md)
  Gets the specified extended attribute of the given item.
- [func listXattrs(of: FSItem, replyHandler: ([FSFileName]?, (any Error)?) -> Void)](fsvolume/xattroperations/listxattrs(of:replyhandler:).md)
  Gets the list of extended attributes currently set on the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler: ((any Error)?) -> Void)](fsvolume/xattroperations/setxattr(named:to:on:policy:replyhandler:).md)
  Sets the specified extended attribute data on the given item.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattroperations/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/setxattrpolicy)*