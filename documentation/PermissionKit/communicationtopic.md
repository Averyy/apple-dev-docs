# CommunicationTopic

**Framework**: PermissionKit  
**Kind**: struct

A topic for requesting communication permission with specific people.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct CommunicationTopic
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

## Topics

### Working with supporting types
- [CommunicationTopic.Action](communicationtopic/action.md)
  A communication action you can request permission for.
- [CommunicationTopic.PersonInformation](communicationtopic/personinformation-swift.struct.md)
  Information about a person the child wants to communicate with.
### Creating topics
- [init(personInformation: [CommunicationTopic.PersonInformation])](communicationtopic/init(personinformation:).md)
  Creates a communication topic with person information for general communication.
- [init(personInformation: [CommunicationTopic.PersonInformation], actions: Set<CommunicationTopic.Action>)](communicationtopic/init(personinformation:actions:).md)
  Creates a communication topic with person information and specific actions.
### Accessing properties
- [var actions: Set<CommunicationTopic.Action>](communicationtopic/actions.md)
  The communication actions the child wants to perform.
- [var personInformation: [CommunicationTopic.PersonInformation]](communicationtopic/personinformation-swift.property.md)
  Information about the people the child wants to communicate with.
- [static let id: String](communicationtopic/id.md)
  The topic’s unique identifier.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [QuestionTopic](questiontopic.md)

## See Also

- [struct SignificantAppUpdateTopic](significantappupdatetopic.md)
  A topic for requesting permission for significant app updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationtopic)*