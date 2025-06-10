# PermissionResponse

**Framework**: PermissionKit  
**Kind**: struct

A full permission response that includes the original question and chosen answer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct PermissionResponse<Topic> where Topic : QuestionTopic
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

## Topics

### Summarizing a permission response
- [let choice: PermissionChoice](permissionresponse/choice.md)
  The choice made by the person initiating this response.
- [let question: PermissionQuestion<Topic>](permissionresponse/question.md)
  The original question that this response answers.

## See Also

- [class CommunicationLimits](communicationlimits.md)
  A type that encapsulates the communication limits for your app.
- [struct CommunicationHandle](communicationhandle.md)
  A piece of identifying information that can be used to communicate with someone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionresponse)*