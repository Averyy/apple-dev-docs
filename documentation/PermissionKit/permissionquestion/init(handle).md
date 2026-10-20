# init(handle:)

**Framework**: PermissionKit  
**Kind**: init  
**Role**: Initializer

Creates a permission question that asks parents or guardians for permission to communicate with a person.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(handle: CommunicationHandle)
```

Available when `Topic` is `CommunicationTopic`.

## Parameters

- `handle`: The communication handle for the person the child wants to communicate with, such as a phone number, email address, or custom identifier.

## See Also

### Creating permission requests
- [convenience init(handles: [CommunicationHandle])](./init%28handles%29.md)
  Creates a permission question that asks parents or guardians for permission to communicate with multiple people.
- [convenience init(communicationTopic: Topic)](./init%28communicationtopic%29.md)
  Creates a permission question that asks parents or guardians for communication permission.
- [convenience init(significantAppUpdateTopic: Topic)](./init%28significantappupdatetopic%29.md)
  Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(handle:))*