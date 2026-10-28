# FSCheckAccessResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a check-access call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSCheckAccessResult
```

```objc
@interface FSCheckAccessResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation of [`checkAccess(to:requestedAccess:context:replyHandler:)`](./fsvolume/accesscheckhandler/checkaccess%28to,requestedaccess,context,replyhandler%29.md).

## Topics

### Creating a check-access result
- [init?(accessAllowed: Bool)](./fscheckaccessresult/init%28accessallowed%29.md)
  Creates a result for an access-checking operation.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Checking access
- [func checkAccess(to: FSItem, requestedAccess: FSVolume.AccessMask, context: FSContext, replyHandler: (FSCheckAccessResult?, (any Error)?) -> Void)](./fsvolume/accesscheckhandler/checkaccess%28to,requestedaccess,context,replyhandler%29.md)
  Checks whether the file system allows access to the given item.
- [FSVolume.AccessMask](./fsvolume/accessmask.md)
  A bitmask of access rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscheckaccessresult)*