# PermissionQuestion

**Framework**: PermissionKit  
**Kind**: class

A class that captures a permission question posed by a user.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class PermissionQuestion<Topic> where Topic : QuestionTopic
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

## Topics

### Initializing an asking experience
- [convenience init(handle: CommunicationHandle)](permissionquestion/init(handle:).md)
  Asks the user’s parents and/or guardians to communicate with someone using their handle or account identifier, with default binary approve/deny choices.
- [convenience init(handles: [CommunicationHandle])](permissionquestion/init(handles:).md)
  Asks the user’s parents and/or guardians to communicate with a set of people using their handle or account identifier, with default binary approve/deny choices.
- [convenience init(communicationTopic: Topic)](permissionquestion/init(communicationtopic:).md)
  Asks the user’s parents and/or guardians to communicate with a set of people with the given metadata.
### Identifying answer choices
- [let id: UUID](permissionquestion/id-swift.property.md)
  A unique identifier for the question.
- [let topic: Topic](permissionquestion/topic.md)
  A topic that can be used to interpret a user’s request.
- [var choices: [PermissionChoice]](permissionquestion/choices.md)
  The possible answer choices associated with this question.
- [var defaultChoice: PermissionChoice](permissionquestion/defaultchoice.md)
  The default answer choice associated with the question.
### Setting an expiration
- [var expirationDate: Date?](permissionquestion/expirationdate.md)
  The date that this question expires, if any. Once this date passes, receivers of this question will be unable to respond.
### Decoding
- [init(from: any Decoder) throws](permissionquestion/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](permissionquestion/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [PermissionQuestion.ID](permissionquestion/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [protocol QuestionTopic](questiontopic.md)
  A protocol that defines a question topic that can be used to interpret what a user is asking for.
- [struct CommunicationTopic](communicationtopic.md)
  A question topic related to communication.
- [struct PermissionChoice](permissionchoice.md)
  A class that uniquely identifies a specific, statically defined permission choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion)*