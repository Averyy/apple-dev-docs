# RCSService.CreateGroupChatRequest.Result

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure representing the result of a request to create a group chat.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Result
```

## Topics

### Accessing result properties
- [let groupHandle: RCSHandle.Group](./result/grouphandle.md)
  Handle for the newly created group.
- [let participants: [RCSHandle.URI]](./result/participants.md)
  Array of participants in group chat.
- [let subject: String?](./result/subject.md)
  The group chat’s subject.
### Supporting RCS encryption
- [let isEndToEndEncrypted: Bool](./result/isendtoendencrypted.md)
  A Boolean value indicating whether the associated group is end-to-end encrypted.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/creategroupchatrequest/result)*