# SignificantAppUpdateTopic

**Framework**: PermissionKit  
**Kind**: struct

A topic for requesting permission for significant app updates.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.2+

## Declaration

```swift
struct SignificantAppUpdateTopic
```

#### Overview

Use `SignificantAppUpdateTopic` when your app has a significant update that requires parents or guardians to consent on behalf of their child. This topic helps you create consistent asking experiences that may comply with regulations that require notification or permission for app changes. You determine what constitutes a significant update based on applicable regulations.

Use concise, understandable language that clearly explains what changed in your app. Parents and guardians see this description when deciding whether to grant permission.

```swift
// Specific
let topic = SignificantAppUpdateTopic(
     description: "This update adds video calling and location sharing features."
)

// Vague
let topic = SignificantAppUpdateTopic(
    description: "We've made improvements to the app."
)
```

## Topics

### Creating topics
- [init(description: String)](significantappupdatetopic/init(description:).md)
  Creates a new significant app update topic with the specified description.
### Accessing properties
- [let description: String](significantappupdatetopic/description.md)
  A description of the significant update that initiates the permission question.
- [static let id: String](significantappupdatetopic/id.md)
  The unique identifier the system uses to categorize this topic type.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [QuestionTopic](questiontopic.md)

## See Also

- [struct CommunicationTopic](communicationtopic.md)
  A topic for requesting communication permission with specific people.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/significantappupdatetopic)*