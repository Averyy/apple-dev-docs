# question

**Framework**: PermissionKit  
**Kind**: property  
**Role**: Instance Property

The question to ask a parent or guardian about making an exception to their child’s communication limits.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency let question: PermissionQuestion<CommunicationTopic>
```

## See Also

### Creating a view
- [init(question: PermissionQuestion<CommunicationTopic>, label: () -> Label)](./init%28question,label%29.md)
  Creates a new instance.
- [var body: some View](./body.md)
  The body of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/question)*