# RCSHandle.URI

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an RCS URI handle.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct URI
```

## Topics

### Creating a URI instance
- [init(stringLiteral: String)](./uri/init%28stringliteral%29.md)
  Creates a URI instance from the given string.
### Working with raw values
- [init(rawValue: String)](./uri/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [let rawValue: String](./uri/rawvalue.md)
  The raw value of the handle

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing handle values
- [case uri(RCSHandle.URI)](./uri%28_%29.md)
  A handle that represents a single recipient or sender, as identified by a URI.
- [case group(RCSHandle.Group)](./group%28_%29.md)
  A handle that represents a group.
- [RCSHandle.Group](./group.md)
  A structure that represents an RCS group handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcshandle/uri)*