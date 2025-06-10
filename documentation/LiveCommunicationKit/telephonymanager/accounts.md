# accounts

**Framework**: LiveCommunicationKit  
**Kind**: property

The list of accounts that an application can use to initiate a conversation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var accounts: [Account] { get }
```

#### Discussion

To have access to accounts, your app needs to be the default calling app. If your app doesn’t have permission to access to accounts, it can still initiate conversations using [`TelephonyManager`](telephonymanager.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/telephonymanager/accounts)*