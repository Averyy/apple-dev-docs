# chatRevokeTimeout

**Framework**: TelephonyMessagingKit  
**Kind**: property

The maximum duration the service provider allows for delivery notification before it revokes a chat message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
let chatRevokeTimeout: Duration?
```

#### Discussion

After the app sends a message, the system expects to receive a delivery notification for that message. When your app sends a message, start a timer with this timeout value. If the timer expires without receiving a delivery notification, revoke the message with [`revokeMessage(_:)`](rcsservice/revokemessage(_:).md), and resend with SMS or MMS.

This value is represented as a Swift [`Duration`](https://developer.apple.com/documentation/Swift/Duration), unless the client can’t send Revoke Message requests, in which case the value is `nil`.

## See Also

- [var maximumGroupSize: Int?](rcsservice/configuration/maximumgroupsize.md)
  The maximum number of participants allowed for a group chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration/chatrevoketimeout)*