# init(communicationTopic:)

**Framework**: PermissionKit  
**Kind**: init

Asks the user’s parents and/or guardians to communicate with a set of people with the given metadata.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(communicationTopic: Topic)
```

## Parameters

- `communicationTopic`: Metadata for the type and set of people to be part of the communication.

## See Also

- [convenience init(handle: CommunicationHandle)](permissionquestion/init(handle:).md)
  Asks the user’s parents and/or guardians to communicate with someone using their handle or account identifier, with default binary approve/deny choices.
- [convenience init(handles: [CommunicationHandle])](permissionquestion/init(handles:).md)
  Asks the user’s parents and/or guardians to communicate with a set of people using their handle or account identifier, with default binary approve/deny choices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(communicationtopic:))*