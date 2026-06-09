# listXattrs(of:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Gets the list of extended attributes currently set on the given item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func xattrs(of item: FSItem, context: FSContext) async throws -> FSListXattrsResult
```

## Parameters

- `item`: The item from which to get extended attributes.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If getting the list of extended attributes succeeds, pass an instance of [`FSListXattrsResult`](fslistxattrsresult.md) containing the xattrs as an array of [`FSFileName`](fsfilename.md) instances, along with a `nil` error. If getting the attributes fails, pass the relevant error as the second parameter; FSKit ignores the [`FSListXattrsResult`](fslistxattrsresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [func getXattr(named: FSFileName, of: FSItem, context: FSContext, replyHandler: (FSGetXattrResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/getxattr(named:of:context:replyhandler:).md)
  Gets the specified extended attribute of the given item.
- [class FSGetXattrResult](fsgetxattrresult.md)
  The result of a get-extended-attributes call.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattrhandler/listxattrs(of:context:replyhandler:))*