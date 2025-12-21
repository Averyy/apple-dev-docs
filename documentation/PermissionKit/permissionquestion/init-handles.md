# init(handles:)

**Framework**: PermissionKit  
**Kind**: init

Creates a permission question that asks parents or guardians for permission to communicate with multiple people.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(handles: [CommunicationHandle])
```

## Parameters

- `handles`: The communication handles for the people the child wants to communicate with, such as phone numbers, email addresses, or custom identifiers.

## See Also

- [convenience init(handle: CommunicationHandle)](permissionquestion/init(handle:).md)
  Creates a permission question that asks parents or guardians for permission to communicate with a person.
- [convenience init(communicationTopic: Topic)](permissionquestion/init(communicationtopic:).md)
  Creates a permission question that asks parents or guardians for communication permission.
- [convenience init(significantAppUpdateTopic: Topic)](permissionquestion/init(significantappupdatetopic:).md)
  Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(handles:))*