# init(handles:)

**Framework**: PermissionKit  
**Kind**: init  
**Role**: Initializer

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

Available when `Topic` is `CommunicationTopic`.

## Parameters

- `handles`: The communication handles for the people the child wants to communicate with, such as phone numbers, email addresses, or custom identifiers.

## See Also

### Creating permission requests
- [convenience init(handle: CommunicationHandle)](./init%28handle%29.md)
  Creates a permission question that asks parents or guardians for permission to communicate with a person.
- [convenience init(communicationTopic: Topic)](./init%28communicationtopic%29.md)
  Creates a permission question that asks parents or guardians for communication permission.
- [convenience init(significantAppUpdateTopic: Topic)](./init%28significantappupdatetopic%29.md)
  Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(handles:))*