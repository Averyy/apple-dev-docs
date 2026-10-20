# RCSHandle.Group

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an RCS group handle.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Group
```

## Topics

### Accessing group properties
- [let focus: String](./group/focus.md)
  A string that represents the focus of this group, as described in RFC 4353.
- [let conversationID: String](./group/conversationid.md)
  A string that represents the conversation identifier for this group.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing handle values
- [case uri(RCSHandle.URI)](./uri%28_%29.md)
  A handle that represents a single recipient or sender, as identified by a URI.
- [RCSHandle.URI](./uri.md)
  A structure that represents an RCS URI handle.
- [case group(RCSHandle.Group)](./group%28_%29.md)
  A handle that represents a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcshandle/group)*