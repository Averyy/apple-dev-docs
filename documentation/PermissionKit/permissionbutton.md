# PermissionButton

**Framework**: PermissionKit  
**Kind**: struct

A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
@MainActor
@preconcurrency struct PermissionButton<Topic, Label> where Topic : QuestionTopic, Label : View
```

## Topics

### Creating buttons
- [init(question: PermissionQuestion<Topic>, label: () -> Label)](permissionbutton/init(question:label:)-25jfa.md)
  Creates a button that requests permission from parents or guardians.
- [init(question: PermissionQuestion<Topic>, label: () -> Label)](permissionbutton/init(question:label:)-8291n.md)
  Creates a button that requests permission from parents or guardians to continue using your app after a significant update.
### Accessing properties
- [let question: PermissionQuestion<Topic>](permissionbutton/question.md)
  The question to ask a parent or guardian about making an exception to their child’s communication limits.
- [var body: some View](permissionbutton/body.md)
  The body of the view.
### Initializers
- [init(question: PermissionQuestion<Topic>, permissionFlow: PermissionFlow, onPermissionResult: (Result<PermissionResult, any Error>) -> Void, label: () -> Label)](permissionbutton/init(question:permissionflow:onpermissionresult:label:).md)
  Creates a button that requests permission from parents or guardians, presenting a specific permission flow and reporting the outcome to a completion handler.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [View](../swiftui/view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionbutton)*