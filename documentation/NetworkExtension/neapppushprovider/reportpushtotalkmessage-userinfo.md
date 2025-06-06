# reportPushToTalkMessage(userInfo:)

**Framework**: Network Extension  
**Kind**: method

Informs the manager about a push-to-talk message on the connection.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- visionOS 1.0+

## Declaration

```swift
func reportPushToTalkMessage(userInfo: [AnyHashable : Any] = [:])
```

## Parameters

- `userInfo`: A dictionary of custom information associated with the push-to -talk message, such as the active remote participant. The containing app’s   receives this dictionary if the user has joined a push-to-talk channel.

## See Also

- [func reportIncomingCall(userInfo: [AnyHashable : Any])](neapppushprovider/reportincomingcall(userinfo:).md)
  Informs the manager about an incoming call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/reportpushtotalkmessage(userinfo:))*