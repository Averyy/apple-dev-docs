# PermissionResult

**Framework**: PermissionKit  
**Kind**: enum

Represents the outcome of the permission flow.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum PermissionResult
```

## Topics

### Enumeration Cases
- [PermissionResult.approveInPerson(approved:)](permissionresult/approveinperson(approved:).md)
  The user tapped “Approve in Person” and finalized an answer choice.
- [PermissionResult.askToApprove(didSend:)](permissionresult/asktoapprove(didsend:).md)
  The user tapped “Ask to Approve” and sent the message.
- [PermissionResult.cancel](permissionresult/cancel.md)
  The user cancelled the flow.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionresult)*