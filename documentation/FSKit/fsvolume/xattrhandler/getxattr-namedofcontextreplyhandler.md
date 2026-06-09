# getXattr(named:of:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Gets the specified extended attribute of the given item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func xattr(named name: FSFileName, of item: FSItem, context: FSContext) async throws -> FSGetXattrResult
```

## Parameters

- `name`: The extended attribute name.
- `item`: The item for which to get the extended attribute.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If getting the attribute succeeds, pass an instance of [`FSGetXattrResult`](fsgetxattrresult.md) containing the extended attribute data, along with a `nil` error. If getting the attribute fails, pass the relevant error as the second parameter; FSKit ignores the [`FSGetXattrResult`](fsgetxattrresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

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
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattrhandler/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattrhandler/getxattr(named:of:context:replyhandler:))*