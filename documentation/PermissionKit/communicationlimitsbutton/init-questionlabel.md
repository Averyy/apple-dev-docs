# init(question:label:)

**Framework**: PermissionKit  
**Kind**: init

Creates a new instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+
- Unknown ?+ - Deprecated
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(question: PermissionQuestion<CommunicationTopic>, @ViewBuilder label: @escaping () -> Label)
```

## Parameters

- `question`: The question to ask the person about their communication limits.
- `label`: The view to display as content.

## See Also

- [var body: some View](communicationlimitsbutton/body.md)
  The body of the view.
- [let question: PermissionQuestion<CommunicationTopic>](communicationlimitsbutton/question.md)
  The question to ask a parent or guardian about making an exception to their child’s communication limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/init(question:label:))*