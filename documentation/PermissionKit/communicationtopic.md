# CommunicationTopic

**Framework**: PermissionKit  
**Kind**: struct

A question topic related to communication.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CommunicationTopic
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

## Topics

### Creating a communication topic
- [init(personInformation: [CommunicationTopic.PersonInformation])](communicationtopic/init(personinformation:).md)
  Creates a new topic.
- [init(personInformation: [CommunicationTopic.PersonInformation], actions: Set<CommunicationTopic.Action>)](communicationtopic/init(personinformation:actions:).md)
  Creates a new topic.
- [var actions: Set<CommunicationTopic.Action>](communicationtopic/actions.md)
  The specific communication action to be performed, if any.
- [CommunicationTopic.Action](communicationtopic/action.md)
  A communication action to be performed.
- [static let id: String](communicationtopic/id.md)
  The topic’s unique identifier.
### Identifying metadata
- [var personInformation: [CommunicationTopic.PersonInformation]](communicationtopic/personinformation-swift.property.md)
  The metadata of the people with whom to communicate.
- [CommunicationTopic.PersonInformation](communicationtopic/personinformation-swift.struct.md)
  Metadata corresponding to a specific person.
### Decoding
- [init(from: any Decoder) throws](communicationtopic/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](communicationtopic/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [QuestionTopic](questiontopic.md)

## See Also

- [protocol QuestionTopic](questiontopic.md)
  A protocol that defines a question topic that can be used to interpret what a user is asking for.
- [class PermissionQuestion](permissionquestion.md)
  A class that captures a permission question posed by a user.
- [struct PermissionChoice](permissionchoice.md)
  A class that uniquely identifies a specific, statically defined permission choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationtopic)*