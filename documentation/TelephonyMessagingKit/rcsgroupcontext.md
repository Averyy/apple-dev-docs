# RCSGroupContext

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing information about a message’s group.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct RCSGroupContext
```

## Topics

### Accessing group context properties
- [let handle: RCSHandle.Group](rcsgroupcontext/handle.md)
### Encoding and decoding
- [init(from: any Decoder) throws](rcsgroupcontext/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSGroupContext, RCSGroupContext) -> Bool](rcsgroupcontext/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsgroupcontext/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](rcsgroupcontext/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct RCSFileTransferMetadata](rcsfiletransfermetadata.md)
  A structure that contains metadata about an RCS file transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsgroupcontext)*