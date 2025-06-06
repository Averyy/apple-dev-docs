# listXattrs(of:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Gets the list of extended attributes currently set on the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func xattrs(of item: FSItem) async throws -> [FSFileName]
```

## Parameters

- `item`: The item from which to get extended attributes.
- `reply`: A block or closure to indicate success or failure. If getting the list of extended attributes succeeds, pass the xattrs as an array of   instances and a   error. If getting the attriubtes fails, pass   along with the relevant error. For an   Swift implementation, there’s no reply handler; simply return the byte count or throw an error.

## See Also

- [func getXattr(named: FSFileName, of: FSItem, replyHandler: (Data?, (any Error)?) -> Void)](fsvolume/xattroperations/getxattr(named:of:replyhandler:).md)
  Gets the specified extended attribute of the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler: ((any Error)?) -> Void)](fsvolume/xattroperations/setxattr(named:to:on:policy:replyhandler:).md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattroperations/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/listxattrs(of:replyhandler:))*