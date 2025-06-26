# messages(of:for:bufferSize:)

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
func messages<Identifier, Message>(of subject: Message.Subject, for identifier: Identifier, bufferSize limit: Int = 10) -> some AsyncSequence<Message, Never> where Identifier : NotificationCenter.MessageIdentifier, Message : NotificationCenter.AsyncMessage, Message == Identifier.MessageType, Message.Subject : AnyObject
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messages(of:for:buffersize:)-4tof0)*