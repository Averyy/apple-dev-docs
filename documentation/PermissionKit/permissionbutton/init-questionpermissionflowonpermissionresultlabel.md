# init(question:permissionFlow:onPermissionResult:label:)

**Framework**: PermissionKit  
**Kind**: init

Creates a button that requests permission from parents or guardians, presenting a specific permission flow and reporting the outcome to a completion handler.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(question: PermissionQuestion<Topic>, permissionFlow: PermissionFlow, onPermissionResult: @escaping (Result<PermissionResult, any Error>) -> Void, @ViewBuilder label: @escaping () -> Label) where Topic == SignificantAppUpdateTopic
```

## Parameters

- `question`: The question to ask a parent or guardian on behalf of their child.
- `permissionFlow`: The permission flow to present.
- `onPermissionResult`: A closure that’s called with the result of the permission flow. The button is disabled while a flow is presented, so the closure is invoked once per completed interaction.
- `label`: The view to display inside the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionbutton/init(question:permissionflow:onpermissionresult:label:))*