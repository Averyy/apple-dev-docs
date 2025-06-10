# init(handle:)

**Framework**: PermissionKit  
**Kind**: init

Asks the user’s parents and/or guardians to communicate with someone using their handle or account identifier, with default binary approve/deny choices.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(handle: CommunicationHandle)
```

## Parameters

- `handle`: A unique identifier for a person such as a phone number, email address, or custom user name.

## See Also

- [convenience init(handles: [CommunicationHandle])](permissionquestion/init(handles:).md)
  Asks the user’s parents and/or guardians to communicate with a set of people using their handle or account identifier, with default binary approve/deny choices.
- [convenience init(communicationTopic: Topic)](permissionquestion/init(communicationtopic:).md)
  Asks the user’s parents and/or guardians to communicate with a set of people with the given metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(handle:))*