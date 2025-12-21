# CommunicationLimitsButton

**Framework**: PermissionKit  
**Kind**: struct

A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits.

**Availability**:
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- Unknown ?+ - Deprecated
- iOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct CommunicationLimitsButton<Label> where Label : View
```

## Topics

### Creating a view
- [init(question: PermissionQuestion<CommunicationTopic>, label: () -> Label)](communicationlimitsbutton/init(question:label:).md)
  Creates a new instance.
- [var body: some View](communicationlimitsbutton/body.md)
  The body of the view.
- [let question: PermissionQuestion<CommunicationTopic>](communicationlimitsbutton/question.md)
  The question to ask a parent or guardian about making an exception to their child’s communication limits.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton)*