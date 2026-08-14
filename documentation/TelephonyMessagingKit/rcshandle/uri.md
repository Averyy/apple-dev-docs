# RCSHandle.URI

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an RCS URI handle.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct URI
```

## Topics

### Creating a URI instance
- [init(stringLiteral: String)](rcshandle/uri/init(stringliteral:).md)
  Creates a URI instance from the given string.
### Working with raw values
- [init(rawValue: String)](rcshandle/uri/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [let rawValue: String](rcshandle/uri/rawvalue.md)
  The raw value of the handle

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case uri(RCSHandle.URI)](rcshandle/uri(_:).md)
  A handle that represents a single recipient or sender, as identified by a URI.
- [case group(RCSHandle.Group)](rcshandle/group(_:).md)
  A handle that represents a group.
- [RCSHandle.Group](rcshandle/group.md)
  A structure that represents an RCS group handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcshandle/uri)*