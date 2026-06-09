# setXattr(named:to:on:policy:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Sets the specified extended attribute data on the given item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func setXattr(named name: FSFileName, to value: Data?, on item: FSItem, policy: FSVolume.SetXattrPolicy, context: FSContext) async throws -> FSSetXattrResult
```

## Parameters

- `name`: The extended attribute name.
- `value`: The extended attribute value to set. This can’t be `nil`, unless the policy is [`FSVolume.SetXattrPolicy.delete`](fsvolume/setxattrpolicy/delete.md).
- `item`: The item on which to set the extended attribute.
- `policy`: The policy to apply when setting the attribute. See [`FSVolume.SetXattrPolicy`](fsvolume/setxattrpolicy.md) for possible values.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If setting the attribute succeeds, pass an instance of [`FSSetXattrResult`](fssetxattrresult.md) containing the volume’s updated free space, along with a `nil` error. If setting the attribute fails, pass the relevant error as the second parameter; FSKit ignores the [`FSSetXattrResult`](fssetxattrresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [func getXattr(named: FSFileName, of: FSItem, context: FSContext, replyHandler: (FSGetXattrResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/getxattr(named:of:context:replyhandler:).md)
  Gets the specified extended attribute of the given item.
- [class FSGetXattrResult](fsgetxattrresult.md)
  The result of a get-extended-attributes call.
- [func listXattrs(of: FSItem, context: FSContext, replyHandler: (FSListXattrsResult?, (any Error)?) -> Void)](fsvolume/xattrhandler/listxattrs(of:context:replyhandler:).md)
  Gets the list of extended attributes currently set on the given item.
- [class FSListXattrsResult](fslistxattrsresult.md)
  The result of a list-extended-attributes call.
- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [class FSSetXattrResult](fssetxattrresult.md)
  The result of a set-extended-attributes call.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattrhandler/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattrhandler/setxattr(named:to:on:policy:context:replyhandler:))*