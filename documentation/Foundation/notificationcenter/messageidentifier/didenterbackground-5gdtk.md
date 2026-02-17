# didEnterBackground

**Framework**: Foundation  
**Kind**: property

An identifier for a message about a host app beginning to run in the background.

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
static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidEnterBackgroundMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`NSExtensionContext.DidEnterBackgroundMessage`](nsextensioncontext/didenterbackgroundmessage.md).

## See Also

- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidBecomeActiveMessage>](notificationcenter/messageidentifier/didbecomeactive-79dvm.md)
  An identifier for a message about a host app moving from the inactive to the active state.
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillResignActiveMessage>](notificationcenter/messageidentifier/willresignactive-9z4xc.md)
  An identifier for a message about a host app moving from the active to the inactive state.
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillEnterForegroundMessage>](notificationcenter/messageidentifier/willenterforeground-p1og.md)
  An identifier for a message about a host app preparing to run in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didenterbackground-5gdtk)*