# PermissionResult

**Framework**: PermissionKit  
**Kind**: enum  
**Role**: Enumeration

Represents the outcome of the permission flow.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum PermissionResult
```

## Topics

### Enumeration Cases
- [PermissionResult.approveInPerson(approved:)](./permissionresult/approveinperson%28approved%29.md)
  The user tapped “Approve in Person” and finalized an answer choice.
- [PermissionResult.askToApprove(didSend:)](./permissionresult/asktoapprove%28didsend%29.md)
  The user tapped “Ask to Approve” and sent the message.
- [PermissionResult.cancel](./permissionresult/cancel.md)
  The user cancelled the flow.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionresult)*