# addObserver(of:for:using:)

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
func addObserver<Identifier, Message>(of subject: Message.Subject, for identifier: Identifier, using observer: @escaping (Message) async -> Void) -> NotificationCenter.ObservationToken where Identifier : NotificationCenter.MessageIdentifier, Message : NotificationCenter.AsyncMessage, Message == Identifier.MessageType, Message.Subject : AnyObject
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/addobserver(of:for:using:)-twm3)*