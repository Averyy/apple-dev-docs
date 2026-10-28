# reportIncomingCall(userInfo:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Informs the manager about an incoming call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func reportIncomingCall(userInfo: [AnyHashable : Any] = [:])
```

```objc
- (void) reportIncomingCallWithUserInfo:(NSDictionary *) userInfo;
```

## Discussion

Call this method when your provider determines it’s receiving an incoming call on the connection. The manager’s delegate receives this dictionary as-is.

## Parameters

- `userInfo`: A dictionary of custom information associated with the incoming call. The dictionary’s values must only use data types supported by [`PropertyListSerialization`](../../Foundation/propertylistserialization.md); you can’t use custom types for the values.

## See Also

### Receiving local events
- [func reportPushToTalkMessage(userInfo: [AnyHashable : Any])](./reportpushtotalkmessage%28userinfo%29.md)
  Informs the manager about a push-to-talk message on the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/reportincomingcall(userinfo:))*