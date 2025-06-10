# post(_:subject:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func post<Message>(_ message: Message, subject: Message.Subject.Type = Message.Subject.self) where Message : NotificationCenter.MainActorMessage
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/post(_:subject:)-3eb69)*