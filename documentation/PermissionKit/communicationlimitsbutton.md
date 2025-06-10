# CommunicationLimitsButton

**Framework**: PermissionKit  
**Kind**: struct

A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct CommunicationLimitsButton<Label> where Label : View
```

## Topics

### Creating a view
- [init(question: PermissionQuestion<CommunicationTopic>, label: () -> Label)](communicationlimitsbutton/init(question:label:).md)
  Creates a new instance.
- [var body: some View](communicationlimitsbutton/body-swift.property.md)
  The body of the view.
- [let question: PermissionQuestion<CommunicationTopic>](communicationlimitsbutton/question.md)
  The question to ask a parent or guardian about making an exception to their child’s communication limits.
### Type Aliases
- [CommunicationLimitsButton.Body](communicationlimitsbutton/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](communicationlimitsbutton/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton)*