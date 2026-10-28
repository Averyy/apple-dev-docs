# didLoad

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An identifier for a message about a bundle dynamically loading a class.

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
static var didLoad: NotificationCenter.BaseMessageIdentifier<Bundle.DidLoadMessage> { get }
```

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<Bundle.DidLoadMessage>`.

## Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`Bundle.DidLoadMessage`](../../bundle/didloadmessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didload)*