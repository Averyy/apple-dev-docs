# init(handle:)

**Framework**: PermissionKit  
**Kind**: init

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

## Parameters

- `handle`: The communication handle for the person the child wants to communicate with, such as a phone number, email address, or custom identifier.

## See Also

- [convenience init(handles: [CommunicationHandle])](permissionquestion/init(handles:).md)
  Creates a permission question that asks parents or guardians for permission to communicate with multiple people.
- [convenience init(communicationTopic: Topic)](permissionquestion/init(communicationtopic:).md)
  Creates a permission question that asks parents or guardians for communication permission.
- [convenience init(significantAppUpdateTopic: Topic)](permissionquestion/init(significantappupdatetopic:).md)
  Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(handle:))*