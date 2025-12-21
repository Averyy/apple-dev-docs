# PermissionResponse

**Framework**: PermissionKit  
**Kind**: struct

A full permission response that includes the original question and chosen answer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct PermissionResponse<Topic> where Topic : QuestionTopic
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

## Topics

### Getting response information
- [let choice: PermissionChoice](permissionresponse/choice.md)
  The choice made by the person initiating this response.
- [let question: PermissionQuestion<Topic>](permissionresponse/question.md)
  The original question that this response answers.

## See Also

- [func responses<Topic>(for: Topic.Type) -> some AsyncSequence<PermissionResponse<Topic>, Never>
](askcenter/responses(for:).md)
  Registers the topic type with the system and returns an asynchronous sequence of responses.
- [struct CommunicationHandle](communicationhandle.md)
  Contact information for identifying and communicating with a person.
- [struct PermissionChoice](permissionchoice.md)
  A class that uniquely identifies a specific, statically defined permission choice.
- [class CommunicationLimits](communicationlimits.md)
  A type that encapsulates the communication limits for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionresponse)*