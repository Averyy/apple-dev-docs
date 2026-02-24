# RCSService.CreateGroupChatRequest.Result

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure representing the result of a request to create a group chat.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Result
```

## Topics

### Accessing result properties
- [let groupHandle: RCSHandle.Group](rcsservice/creategroupchatrequest/result/grouphandle.md)
  Handle for the newly created group.
- [let participants: [RCSHandle.URI]](rcsservice/creategroupchatrequest/result/participants.md)
  Array of participants in group chat.
- [let subject: String?](rcsservice/creategroupchatrequest/result/subject.md)
  The group chat’s subject.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/creategroupchatrequest/result)*