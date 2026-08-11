# PermissionFlow

**Framework**: PermissionKit  
**Kind**: enum

Specifies which permission flow to present.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum PermissionFlow
```

## Topics

### Enumeration Cases
- [PermissionFlow.acknowledgmentAlert](permissionflow/acknowledgmentalert.md)
  Presents the “Ask to Approve / Approve in Person / Cancel” acknowledgment alert first, then routes the user into the chosen path.
- [PermissionFlow.approveInPerson](permissionflow/approveinperson.md)
  Goes directly to the Approve-in-Person flow, prompting the user for the Screen Time passcode.
- [PermissionFlow.askToApprove](permissionflow/asktoapprove.md)
  Goes directly to the Messages compose sheet for the “Ask to Approve” flow.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionflow)*