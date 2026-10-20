# init(communicationTopic:)

**Framework**: PermissionKit  
**Kind**: init

Creates a permission question that asks parents or guardians for communication permission.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(communicationTopic: Topic)
```

## Parameters

- `communicationTopic`: The communication topic containing person information and requested actions.

## See Also

- [convenience init(handle: CommunicationHandle)](permissionquestion/init(handle:).md)
  Creates a permission question that asks parents or guardians for permission to communicate with a person.
- [convenience init(handles: [CommunicationHandle])](permissionquestion/init(handles:).md)
  Creates a permission question that asks parents or guardians for permission to communicate with multiple people.
- [convenience init(significantAppUpdateTopic: Topic)](permissionquestion/init(significantappupdatetopic:).md)
  Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(communicationtopic:))*