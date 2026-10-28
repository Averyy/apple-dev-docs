# channel(_:)

**Framework**: ActivityKit  
**Kind**: method  
**Role**: Type Method

A constant to configure a Live Activity that updates its dynamic content for broadcast channels.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
static func channel(_ name: String) -> PushType
```

## Overview

The channel ID is a base64-encoded string. For information on creating a channel, refer to [Sending channel management requests to APNs](../../UserNotifications/sending-channel-management-requests-to-apns.md). The code snippet below is an example of how to specify that you want to use a broadcast push channel.

```swift
Activity.request(attributes: attributes, 
content: content,
pushType: .channel("c29tZUNoYW5uZWw="))
```

## See Also

### Supporting ActivityKit push notifications
- [static var token: PushType](./token.md)
  A constant you use to configure a Live Activity that updates its dynamic content by receiving ActivityKit push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/pushtype/channel(_:))*