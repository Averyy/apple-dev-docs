# isConfiguredForCarrierMessaging

**Framework**: TelephonyMessagingKit  
**Kind**: property

A Boolean value that indicates whether this app is configured to perform carrier messaging operations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final var isConfiguredForCarrierMessaging: Bool { get }
```

## Mentions

- [Creating a carrier messaging app](../availability/creating-a-carrier-messaging-app.md)

#### Discussion

This value is `true` if the app is configured for carrier messaging operations; `false` if not, or if the system can’t determine the app’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/telephonymessagingsession/isconfiguredforcarriermessaging)*