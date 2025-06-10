# RCSHandle.Group

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an RCS group handle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

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
### Encoding and decoding
- [init(from: any Decoder) throws](rcshandle/group/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSHandle.Group, RCSHandle.Group) -> Bool](rcshandle/group/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcshandle/group/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcshandle/group/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcshandle/group/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcshandle/group/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case uri(RCSHandle.URI)](rcshandle/uri(_:).md)
  A handle that represents a single recipient or sender, as identified by a URI.
- [RCSHandle.URI](rcshandle/uri.md)
  A structure that represents an RCS URI handle.
- [case group(RCSHandle.Group)](rcshandle/group(_:).md)
  A handle that represents a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcshandle/group)*