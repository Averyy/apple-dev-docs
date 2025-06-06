# getXattr(named:of:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Gets the specified extended attribute of the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func xattr(named name: FSFileName, of item: FSItem) async throws -> Data
```

## Parameters

- `name`: The extended attribute name.
- `item`: The item for which to get the extended attribute.
- `reply`: A block or closure to indicate success or failure. If getting the attribute succeeds, pass an data instance containing the extended attribute data and a   error. If getting the attribute fails, pass the relevant error as the second parameter; FSKit ignores any data in this case. For an   Swift implementation, there’s no reply handler; simply return the data or throw an error.

## See Also

- [func listXattrs(of: FSItem, replyHandler: ([FSFileName]?, (any Error)?) -> Void)](fsvolume/xattroperations/listxattrs(of:replyhandler:).md)
  Gets the list of extended attributes currently set on the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler: ((any Error)?) -> Void)](fsvolume/xattroperations/setxattr(named:to:on:policy:replyhandler:).md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattroperations/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/getxattr(named:of:replyhandler:))*