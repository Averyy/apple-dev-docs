# supportedXattrNames(for:)

**Framework**: FSKit  
**Kind**: method

Returns an array that specifies the extended attribute names the given item supports.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func supportedXattrNames(for item: FSItem) -> [FSFileName]
```

#### Discussion

If `item` supports no extended attributes, this method returns `nil`.

Only implement this method if your volume works with “limited” extended attributes. For purposes of this protocol, “limited” support means the volume doesn’t support extended attributes generally, but uses these APIs to expose specific file system data.

> **Note**: If a file system implements this method, FSKit assumes limited support for extended attributes exists. In this mode, FSkit only calls this protocol’s methods for the extended attribute names this method returns.

## Parameters

- `item`: The item for which to get information.

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
- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [class FSSetXattrResult](fssetxattrresult.md)
  The result of a set-extended-attributes call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattrhandler/supportedxattrnames(for:))*