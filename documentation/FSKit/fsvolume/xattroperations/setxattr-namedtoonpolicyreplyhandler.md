# setXattr(named:to:on:policy:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Sets the specified extended attribute data on the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func setXattr(named name: FSFileName, to value: Data?, on item: FSItem, policy: FSVolume.SetXattrPolicy) async throws
```

## Parameters

- `name`: The extended attribute name.
- `value`: The extended attribute value to set. This can’t be  , unless the policy is  .
- `item`: The item on which to set the extended attribute.
- `policy`: The policy to apply when setting the attribute. See   for possible values.
- `reply`: A block or closure to indicate success or failure. If setting the attribute fails, pass an error as the one parameter to the reply handler. If setting the attribute succeeds, pass  . For an   Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

- [func getXattr(named: FSFileName, of: FSItem, replyHandler: (Data?, (any Error)?) -> Void)](fsvolume/xattroperations/getxattr(named:of:replyhandler:).md)
  Gets the specified extended attribute of the given item.
- [func listXattrs(of: FSItem, replyHandler: ([FSFileName]?, (any Error)?) -> Void)](fsvolume/xattroperations/listxattrs(of:replyhandler:).md)
  Gets the list of extended attributes currently set on the given item.
- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattroperations/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/setxattr(named:to:on:policy:replyhandler:))*