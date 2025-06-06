# appPushManager(_:didReceiveIncomingCallWithUserInfo:)

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

A delegate method that the framework invokes when the provider reports an incoming call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func appPushManager(_ manager: NEAppPushManager, didReceiveIncomingCallWithUserInfo userInfo: [AnyHashable : Any] = [:])
```

#### Discussion

The framwork calls this method on your delegate when the provider calls the [`reportIncomingCall(userInfo:)`](neapppushprovider/reportincomingcall(userinfo:).md) method.

## Parameters

- `manager`: The local push manager that receives the call.
- `userInfo`: A dictionary of custom information that the provider supplied in its call to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushdelegate/apppushmanager(_:didreceiveincomingcallwithuserinfo:))*