# RCSGroupContext

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing information about a message’s group.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct RCSGroupContext
```

## Topics

### Accessing group context properties
- [let handle: RCSHandle.Group](./rcsgroupcontext/handle.md)
  The handle associated with the group.
### Supporting RCS encryption
- [let isEndToEndEncrypted: Bool](./rcsgroupcontext/isendtoendencrypted.md)
  A Boolean value that indicates whether the associated group is end-to-end encrypted.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [struct RCSFileTransferMetadata](./rcsfiletransfermetadata.md)
  A structure that contains metadata about an RCS file transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsgroupcontext)*