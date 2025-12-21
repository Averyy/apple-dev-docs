# maximumGroupSize

**Framework**: TelephonyMessagingKit  
**Kind**: property

The maximum number of participants allowed for a group chat.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var maximumGroupSize: Int? { get }
```

#### Discussion

This value is `nil` if group chat is disabled.

## See Also

- [let chatRevokeTimeout: Duration?](rcsservice/configuration/chatrevoketimeout.md)
  The maximum duration the service provider allows for delivery notification before it revokes a chat message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration/maximumgroupsize)*