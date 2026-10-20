# currentLocaleDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An identifier for a message about a change in current locale.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var currentLocaleDidChange: NotificationCenter.BaseMessageIdentifier<Locale.CurrentLocaleDidChangeMessage> { get }
```

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<Locale.CurrentLocaleDidChangeMessage>`.

#### Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`Locale.CurrentLocaleDidChangeMessage`](../../locale/currentlocaledidchangemessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/currentlocaledidchange)*