# init(question:label:)

**Framework**: PermissionKit  
**Kind**: init

Creates a button that requests permission from parents or guardians.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.2+

## Declaration

```swift
@MainActor
@preconcurrency init(question: PermissionQuestion<Topic>, @ViewBuilder label: @escaping () -> Label) where Topic == CommunicationTopic
```

## Parameters

- `question`: The question to ask a parent or guardian on behalf of their child.
- `label`: The view to display inside the button.

## See Also

- [init(question: PermissionQuestion<Topic>, label: () -> Label)](permissionbutton/init(question:label:)-8291n.md)
  Creates a button that requests permission from parents or guardians to continue using your app after a significant update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionbutton/init(question:label:)-25jfa)*