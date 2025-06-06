# pushRegistry(_:didUpdate:for:)

**Framework**: PushKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the system updated the credentials for the specified type of push notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func pushRegistry(_ registry: PKPushRegistry, didUpdate pushCredentials: PKPushCredentials, for type: PKPushType)
```

## Mentions

- [Supporting PushKit Notifications in Your App](supporting-pushkit-notifications-in-your-app.md)

#### Discussion

The system calls this method when it receives new credentials (including a push token) for the specified push type.

## Parameters

- `registry`: The   instance responsible for the delegate callback.
- `type`: One of the requested notification types. This type is present in the   property of the push registry.

## See Also

- [func pushRegistry(PKPushRegistry, didInvalidatePushTokenFor: PKPushType)](pkpushregistrydelegate/pushregistry(_:didinvalidatepushtokenfor:).md)
  Tells the delegate that the system invalidated the push token for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/pushregistry(_:didupdate:for:))*