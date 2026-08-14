# RCSHandle.Group

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an RCS group handle.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Group
```

## Topics

### Accessing group properties
- [let focus: String](rcshandle/group/focus.md)
  A string that represents the focus of this group, as described in RFC 4353.
- [let conversationID: String](rcshandle/group/conversationid.md)
  A string that represents the conversation identifier for this group.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case uri(RCSHandle.URI)](rcshandle/uri(_:).md)
  A handle that represents a single recipient or sender, as identified by a URI.
- [RCSHandle.URI](rcshandle/uri.md)
  A structure that represents an RCS URI handle.
- [case group(RCSHandle.Group)](rcshandle/group(_:).md)
  A handle that represents a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcshandle/group)*