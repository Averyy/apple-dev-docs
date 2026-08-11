# askSignificantChangePermission(for:permissionFlow:in:)

**Framework**: PermissionKit  
**Kind**: method

Requests that a child send the significant app update permission question to their parent or guardian using the specified permission flow.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func askSignificantChangePermission(for question: PermissionQuestion<SignificantAppUpdateTopic>, permissionFlow: PermissionFlow, in viewController: UIViewController) async throws -> PermissionResult
```

#### Return Value

The user’s resolved action — `.askToApprove(didSend:)`, `.approveInPerson(approved:)`, or `.cancel`.

#### Discussion

Throws an error if the system can’t request a child to send the permission question.

## Parameters

- `question`: The question that the system requests the child send.
- `permissionFlow`: The permission flow to present.
- `viewController`: The view controller to which to anchor and present system UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askcenter/asksignificantchangepermission(for:permissionflow:in:)-nm9w)*