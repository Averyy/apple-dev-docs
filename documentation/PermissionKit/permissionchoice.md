# PermissionChoice

**Framework**: PermissionKit  
**Kind**: struct

A class that uniquely identifies a specific, statically defined permission choice.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct PermissionChoice
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

#### Overview

Each [`PermissionQuestion`](permissionquestion.md) contains a set of possible answer choices, each corresponding to a globally unique identifier that you can interpret.

The code below is an example of how to use `PermissionChoice` to set permission choices for a person using your app.

```swift
   let approveOneHour = PermissionChoice(id: AnswerIdentifier.approveOneHour,
   title: "Approve for one hour", answer: .approval)
   let approveAllDay = PermissionChoice(id: AnswerIdentifier.approveAllDay,
    title: "Approve all day", answer: .approval)
   let approveIndefinitely = PermissionChoice(id: AnswerIdentifier.approveIndefinitely,
     title: "Approve indefinitely", answer: .approval)
   let decline = PermissionChoice(id: AnswerIdentifier.decline,
                          title: "Decline", answer: .denial)
```

If your application only requires a yes or no response, you can use the two predefined `PermissionChoice` options: [`approve`](permissionchoice/approve.md) and [`decline`](permissionchoice/decline.md).

## Topics

### Accessing answers
- [var answer: PermissionChoice.Answer](permissionchoice/answer-swift.property.md)
  The type of answer this choice represents.
- [PermissionChoice.Answer](permissionchoice/answer-swift.enum.md)
  An answer to the permission request.
- [static let approve: PermissionChoice](permissionchoice/approve.md)
  The system-preferred choice to approve a permission request.
- [static let decline: PermissionChoice](permissionchoice/decline.md)
  The system-preferred choice to decline a permission request.
### Identifying permissions
- [var id: String](permissionchoice/id.md)
  A unique identifier for this choice.
- [var title: String](permissionchoice/title.md)
  The title of the choice that’s displayed to the person by the system.
### Computing hashes
- [func hash(into: inout Hasher)](permissionchoice/hash(into:).md)
  Performs a hash operation on the value by feeding its hash values into the given hasher.
- [static func == (PermissionChoice, PermissionChoice) -> Bool](permissionchoice/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [func responses<Topic>(for: Topic.Type) -> some AsyncSequence<PermissionResponse<Topic>, Never>
](askcenter/responses(for:).md)
  Registers the topic type with the system and returns an asynchronous sequence of responses.
- [struct PermissionResponse](permissionresponse.md)
  A full permission response that includes the original question and chosen answer.
- [struct CommunicationHandle](communicationhandle.md)
  Contact information for identifying and communicating with a person.
- [class CommunicationLimits](communicationlimits.md)
  A type that encapsulates the communication limits for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionchoice)*