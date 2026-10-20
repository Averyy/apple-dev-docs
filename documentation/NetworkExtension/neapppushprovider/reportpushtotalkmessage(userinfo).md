# reportPushToTalkMessage(userInfo:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Informs the manager about a push-to-talk message on the connection.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- visionOS 1.0+

## Declaration

```swift
func reportPushToTalkMessage(userInfo: [AnyHashable : Any] = [:])
```

```objc
- (void) reportPushToTalkMessageWithUserInfo:(NSDictionary *) userInfo;
```

## Parameters

- `userInfo`: A dictionary of custom information associated with the push-to -talk message, such as the active remote participant. The containing app’s [`PTChannelManagerDelegate`](../../PushToTalk/ptchannelmanagerdelegate.md) receives this dictionary if the user has joined a push-to-talk channel.

## See Also

### Receiving local events
- [func reportIncomingCall(userInfo: [AnyHashable : Any])](./reportincomingcall%28userinfo%29.md)
  Informs the manager about an incoming call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/reportpushtotalkmessage(userinfo:))*