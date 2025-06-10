# init(personInformation:actions:)

**Framework**: PermissionKit  
**Kind**: init

Creates a new topic.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(personInformation: [CommunicationTopic.PersonInformation], actions: Set<CommunicationTopic.Action>)
```

## Parameters

- `personInformation`: The metadata of the people with whom to communicate.
- `actions`: The specific communication actions to be performed.

## See Also

- [init(personInformation: [CommunicationTopic.PersonInformation])](communicationtopic/init(personinformation:).md)
  Creates a new topic.
- [var actions: Set<CommunicationTopic.Action>](communicationtopic/actions.md)
  The specific communication action to be performed, if any.
- [CommunicationTopic.Action](communicationtopic/action.md)
  A communication action to be performed.
- [static let id: String](communicationtopic/id.md)
  The topic’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationtopic/init(personinformation:actions:))*