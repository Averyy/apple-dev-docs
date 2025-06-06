# checkAccess(to:requestedAccess:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Checks whether the file system allows access to the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func checkAccess(to theItem: FSItem, requestedAccess access: FSVolume.AccessMask) async throws -> Bool
```

## Parameters

- `theItem`: The item for which to check access.
- `access`: A mask indicating a set of access types for which to check.
- `reply`: A block or closure to indicate success or failure. If the access check succeeds, pass a Boolean value to indicate whether the file system grants access, followed by a   error. If the access check fails, pass the relevant error as the second parameter; FSKit ignores the Boolean parameter in this case. For an   Swift implementation, there’s no reply handler; simply return the   or throw an error.

## See Also

- [FSVolume.AccessMask](fsvolume/accessmask.md)
  A bitmask of access rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accesscheckoperations/checkaccess(to:requestedaccess:replyhandler:))*