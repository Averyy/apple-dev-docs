# PermissionQuestion

**Framework**: PermissionKit  
**Kind**: class

A class that captures a permission question posed by a person.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class PermissionQuestion<Topic> where Topic : QuestionTopic
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

## Topics

### Creating permission requests
- [convenience init(handle: CommunicationHandle)](permissionquestion/init(handle:).md)
  Creates a permission question that asks parents or guardians for permission to communicate with a person.
- [convenience init(handles: [CommunicationHandle])](permissionquestion/init(handles:).md)
  Creates a permission question that asks parents or guardians for permission to communicate with multiple people.
- [convenience init(communicationTopic: Topic)](permissionquestion/init(communicationtopic:).md)
  Creates a permission question that asks parents or guardians for communication permission.
- [convenience init(significantAppUpdateTopic: Topic)](permissionquestion/init(significantappupdatetopic:).md)
  Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.
### Working with choices
- [var choices: [PermissionChoice]](permissionquestion/choices.md)
  The possible answer choices associated with this question.
- [var defaultChoice: PermissionChoice](permissionquestion/defaultchoice.md)
  The default answer choice associated with the question.
### Accessing properties
- [let id: UUID](permissionquestion/id.md)
  A unique identifier for the question.
- [let topic: Topic](permissionquestion/topic.md)
  A topic that can be used to interpret a person’s request.
- [var expirationDate: Date?](permissionquestion/expirationdate.md)
  The date that this question expires, if any.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [Creating a communication experience](creating-a-communication-experience.md)
  Request permission from a parent or guardian to modify a child’s communication rules.
- [class AskCenter](askcenter.md)
  A class that manages permission requests you send to parents or guardians for approval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion)*