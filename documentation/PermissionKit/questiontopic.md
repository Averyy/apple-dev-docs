# QuestionTopic

**Framework**: PermissionKit  
**Kind**: protocol

A protocol that defines a question topic that can be used to interpret what a person is asking for.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

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
- [SignificantAppUpdateTopic](significantappupdatetopic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/questiontopic)*