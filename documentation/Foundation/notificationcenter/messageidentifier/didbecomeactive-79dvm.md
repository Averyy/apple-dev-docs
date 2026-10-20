# didBecomeActive

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An identifier for a message about a host app moving from the inactive to the active state.

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
static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidBecomeActiveMessage> { get }
```

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidBecomeActiveMessage>`.

#### Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`NSExtensionContext.DidBecomeActiveMessage`](../../nsextensioncontext/didbecomeactivemessage.md).

## See Also

### Identifying extension messages
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillResignActiveMessage>](./willresignactive-9z4xc.md)
  An identifier for a message about a host app moving from the active to the inactive state.
- [static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidEnterBackgroundMessage>](./didenterbackground-5gdtk.md)
  An identifier for a message about a host app beginning to run in the background.
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillEnterForegroundMessage>](./willenterforeground-p1og.md)
  An identifier for a message about a host app preparing to run in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didbecomeactive-79dvm)*