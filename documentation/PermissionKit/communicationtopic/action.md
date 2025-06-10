# CommunicationTopic.Action

**Framework**: PermissionKit  
**Kind**: enum

A communication action to be performed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Action
```

## Topics

### Performing a communication action
- [CommunicationTopic.Action.call](communicationtopic/action/call.md)
  A request to call someone.
- [CommunicationTopic.Action.follow](communicationtopic/action/follow.md)
  A request to follow someone.
- [CommunicationTopic.Action.friend](communicationtopic/action/friend.md)
  A request to friend someone.
- [CommunicationTopic.Action.message](communicationtopic/action/message.md)
  A request to message someone.
- [CommunicationTopic.Action.videoChat](communicationtopic/action/videochat.md)
  A request to video chat with someone.
### Decoding
- [init(from: any Decoder) throws](communicationtopic/action/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (CommunicationTopic.Action, CommunicationTopic.Action) -> Bool](communicationtopic/action/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](communicationtopic/action/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](communicationtopic/action/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](communicationtopic/action/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](communicationtopic/action/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init(personInformation: [CommunicationTopic.PersonInformation])](communicationtopic/init(personinformation:).md)
  Creates a new topic.
- [init(personInformation: [CommunicationTopic.PersonInformation], actions: Set<CommunicationTopic.Action>)](communicationtopic/init(personinformation:actions:).md)
  Creates a new topic.
- [var actions: Set<CommunicationTopic.Action>](communicationtopic/actions.md)
  The specific communication action to be performed, if any.
- [static let id: String](communicationtopic/id.md)
  The topic’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationtopic/action)*