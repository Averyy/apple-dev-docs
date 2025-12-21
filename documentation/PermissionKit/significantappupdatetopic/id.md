# id

**Framework**: PermissionKit  
**Kind**: property

The unique identifier the system uses to categorize this topic type.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.2+

## Declaration

```swift
static let id: String
```

#### Discussion

The system uses this identifier to group related permission requests and ensure your app receives responses for questions with this topic. You don’t need to modify this value - the system handles topic routing automatically using this predefined identifier.

## See Also

- [let description: String](significantappupdatetopic/description.md)
  A description of the significant update that initiates the permission question.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/significantappupdatetopic/id)*