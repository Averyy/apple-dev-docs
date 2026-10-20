# checkAccess(to:requestedAccess:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Checks whether the file system allows access to the given item.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func checkAccess(to theItem: FSItem, requestedAccess access: FSVolume.AccessMask, replyHandler reply: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func checkAccess(to theItem: FSItem, requestedAccess access: FSVolume.AccessMask) async throws -> Bool
```

```objc
- (void) checkAccessToItem:(FSItem *) theItem requestedAccess:(FSAccessMask) access replyHandler:(void (^)(BOOL shouldAllowAccess, NSError *error)) reply;
```

## Parameters

- `theItem`: The item for which to check access.
- `access`: A mask indicating a set of access types for which to check.
- `reply`: A block or closure to indicate success or failure. If the access check succeeds, pass a Boolean value to indicate whether the file system grants access, followed by a `nil` error. If the access check fails, pass the relevant error as the second parameter; FSKit ignores the Boolean parameter in this case. For an `async` Swift implementation, there’s no reply handler; simply return the `Bool` or throw an error.

## See Also

### Checking access
- [FSVolume.AccessMask](../accessmask.md)
  A bitmask of access rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accesscheckoperations/checkaccess(to:requestedaccess:replyhandler:))*