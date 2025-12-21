# PermissionButton

**Framework**: PermissionKit  
**Kind**: struct

A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
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

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionbutton)*