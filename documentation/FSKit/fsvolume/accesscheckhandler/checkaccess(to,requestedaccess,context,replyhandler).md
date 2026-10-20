# checkAccess(to:requestedAccess:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Checks whether the file system allows access to the given item.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func checkAccess(to theItem: FSItem, requestedAccess access: FSVolume.AccessMask, context: FSContext, replyHandler reply: @escaping @Sendable (FSCheckAccessResult?, (any Error)?) -> Void)
```

```swift
func checkAccess(to theItem: FSItem, requestedAccess access: FSVolume.AccessMask, context: FSContext) async throws -> FSCheckAccessResult
```

```objc
- (void) checkAccessToItem:(FSItem *) theItem requestedAccess:(FSAccessMask) access context:(FSContext *) context replyHandler:(void (^)(FSCheckAccessResult *result, NSError *error)) reply;
```

## Parameters

- `theItem`: The item for which to check access.
- `access`: A mask indicating a set of access types for which to check.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If the access check succeeds, pass an instance of [`FSCheckAccessResult`](../../fscheckaccessresult.md) containing a Boolean value to indicate whether the file system grants access, along with a `nil` error. If the access check fails, pass the relevant error as the second parameter; FSKit ignores the [`FSCheckAccessResult`](../../fscheckaccessresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

### Checking access
- [FSVolume.AccessMask](../accessmask.md)
  A bitmask of access rights.
- [class FSCheckAccessResult](../../fscheckaccessresult.md)
  The result of a check-access call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accesscheckhandler/checkaccess(to:requestedaccess:context:replyhandler:))*