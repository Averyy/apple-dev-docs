# FSCheckAccessResult

**Framework**: FSKit  
**Kind**: class

The result of a check-access call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSCheckAccessResult
```

#### Overview

Use this type in your implementation of [`checkAccess(to:requestedAccess:context:replyHandler:)`](fsvolume/accesscheckhandler/checkaccess(to:requestedaccess:context:replyhandler:).md).

## Topics

### Creating a check-access result
- [init?(accessAllowed: Bool)](fscheckaccessresult/init(accessallowed:).md)
  Creates a result for an access-checking operation.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func checkAccess(to: FSItem, requestedAccess: FSVolume.AccessMask, context: FSContext, replyHandler: (FSCheckAccessResult?, (any Error)?) -> Void)](fsvolume/accesscheckhandler/checkaccess(to:requestedaccess:context:replyhandler:).md)
  Checks whether the file system allows access to the given item.
- [FSVolume.AccessMask](fsvolume/accessmask.md)
  A bitmask of access rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscheckaccessresult)*