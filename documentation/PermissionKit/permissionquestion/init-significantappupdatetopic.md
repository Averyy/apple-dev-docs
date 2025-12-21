# init(significantAppUpdateTopic:)

**Framework**: PermissionKit  
**Kind**: init

Creates a permission question that asks parents or guardians for permission to continue using your app after a significant update.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.2+

## Declaration

```swift
convenience init(significantAppUpdateTopic: Topic)
```

## Parameters

- `significantAppUpdateTopic`: The topic describing the significant update that requires permission.

## See Also

- [convenience init(handle: CommunicationHandle)](permissionquestion/init(handle:).md)
  Creates a permission question that asks parents or guardians for permission to communicate with a person.
- [convenience init(handles: [CommunicationHandle])](permissionquestion/init(handles:).md)
  Creates a permission question that asks parents or guardians for permission to communicate with multiple people.
- [convenience init(communicationTopic: Topic)](permissionquestion/init(communicationtopic:).md)
  Creates a permission question that asks parents or guardians for communication permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/init(significantappupdatetopic:))*