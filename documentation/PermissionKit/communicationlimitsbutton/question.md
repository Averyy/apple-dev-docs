# question

**Framework**: PermissionKit  
**Kind**: property

The question to ask a parent or guardian about making an exception to their child’s communication limits.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency let question: PermissionQuestion<CommunicationTopic>
```

## See Also

- [init(question: PermissionQuestion<CommunicationTopic>, label: () -> Label)](communicationlimitsbutton/init(question:label:).md)
  Creates a new instance.
- [var body: some View](communicationlimitsbutton/body-swift.property.md)
  The body of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/question)*