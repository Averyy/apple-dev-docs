# callAsFunction(_:)

**Framework**: PermissionKit  
**Kind**: method

Sends a permission question to a parent or guardian.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)
- macOS 26.5+ (Beta)
- visionOS 26.5+ (Beta)

## Declaration

```swift
@MainActor
func callAsFunction<Topic>(_ question: PermissionQuestion<Topic>) async throws where Topic : QuestionTopic
```

#### Discussion

Call this method to present the system permission request UI. The method throws an error if the system can’t send the permission question.

## Parameters

- `question`: The permission question to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askpermissionaction/callasfunction(_:))*