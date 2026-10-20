# init(significantAppUpdateTopic:)

**Framework**: PermissionKit  
**Kind**: init  
**Role**: Initializer

Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
convenience init(significantAppUpdateTopic: Topic)
```

Available when `Topic` is `SignificantAppUpdateTopic`.

## Parameters

- `significantAppUpdateTopic`: The topic describing the significant update that requires permission.

## See Also

### Creating permission requests
- [convenience init(handle: CommunicationHandle)](./init%28handle%29.md)
  Creates a permission question that asks parents or guardians for permission to communicate with a person.
- [convenience init(handles: [CommunicationHandle])](./init%28handles%29.md)
  Creates a permission question that asks parents or guardians for permission to communicate with multiple people.
- [convenience init(communicationTopic: Topic)](./init%28communicationtopic%29.md)
  Creates a permission question that asks parents or guardians for communication permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(significantappupdatetopic:))*