# channelManager(_:receivedEphemeralPushToken:)

**Framework**: Push to Talk  
**Kind**: method  
**Required**: Yes

Tells the observer that the app received a push token after you create a channel manager.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func channelManager(_ channelManager: PTChannelManager, receivedEphemeralPushToken pushToken: Data)
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

The framework provides a token to this method after you initialize [`PTChannelManager`](ptchannelmanager.md). The token isn’t active until a person joins the channel. If they leave the channel, you need to wait until they rejoin to resume notifications.

> ❗ **Important**:  Don’t cache device tokens in local storage. The Apple Push Notification service issues a new token when a person restores a device from a backup, installs your app on a new device, or reinstalls the operating system.

 Don’t cache device tokens in local storage. The Apple Push Notification service issues a new token when a person restores a device from a backup, installs your app on a new device, or reinstalls the operating system.

When you send push notifications, the `apns-topic` header field needs to contain your app’s bundle identifier wit`h` the `.voip-ptt` suffix.

## Parameters

- `channelManager`: The channel manager.
- `pushToken`: The ephemeral push token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:receivedephemeralpushtoken:))*