# question

**Framework**: PermissionKit  
**Kind**: property

The question to ask a parent or guardian about making an exception to their child’s communication limits.

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
@preconcurrency let question: PermissionQuestion<CommunicationTopic>
```

## See Also

- [init(question: PermissionQuestion<CommunicationTopic>, label: () -> Label)](communicationlimitsbutton/init(question:label:).md)
  Creates a new instance.
- [var body: some View](communicationlimitsbutton/body.md)
  The body of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/question)*