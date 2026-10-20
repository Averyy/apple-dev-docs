# init(communicationTopic:)

**Framework**: PermissionKit  
**Kind**: init  
**Role**: Initializer

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

Available when `Topic` is `CommunicationTopic`.

## Parameters

- `communicationTopic`: The communication topic containing person information and requested actions.

## See Also

### Creating permission requests
- [convenience init(handle: CommunicationHandle)](./init%28handle%29.md)
  Creates a permission question that asks parents or guardians for permission to communicate with a person.
- [convenience init(handles: [CommunicationHandle])](./init%28handles%29.md)
  Creates a permission question that asks parents or guardians for permission to communicate with multiple people.
- [convenience init(significantAppUpdateTopic: Topic)](./init%28significantappupdatetopic%29.md)
  Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(communicationtopic:))*