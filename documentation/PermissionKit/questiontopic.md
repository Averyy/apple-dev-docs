# QuestionTopic

**Framework**: PermissionKit  
**Kind**: protocol

A protocol that defines a question topic that can be used to interpret what a user is asking for.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol QuestionTopic : Decodable, Encodable
```

## Topics

### Getting the topic identifier
- [static var id: String](questiontopic/id.md)
  The unique identifier for the topic.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
### Conforming Types
- [CommunicationTopic](communicationtopic.md)

## See Also

- [class PermissionQuestion](permissionquestion.md)
  A class that captures a permission question posed by a user.
- [struct CommunicationTopic](communicationtopic.md)
  A question topic related to communication.
- [struct PermissionChoice](permissionchoice.md)
  A class that uniquely identifies a specific, statically defined permission choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/questiontopic)*