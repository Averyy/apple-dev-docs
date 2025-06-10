# RCSHandle.URI

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an RCS URI handle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

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
- [let rawValue: String](rcshandle/uri/rawvalue-swift.property.md)
  The raw value of the handle
### Type Aliases
- [RCSHandle.URI.ExtendedGraphemeClusterLiteralType](rcshandle/uri/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [RCSHandle.URI.RawValue](rcshandle/uri/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [RCSHandle.URI.StringLiteralType](rcshandle/uri/stringliteraltype.md)
  A type that represents a string literal.
- [RCSHandle.URI.UnicodeScalarLiteralType](rcshandle/uri/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [Equatable Implementations](rcshandle/uri/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](rcshandle/uri/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](rcshandle/uri/expressiblebystringliteral-implementations.md)
- [RawRepresentable Implementations](rcshandle/uri/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case uri(RCSHandle.URI)](rcshandle/uri(_:).md)
  A handle that represents a single recipient or sender, as identified by a URI.
- [case group(RCSHandle.Group)](rcshandle/group(_:).md)
  A handle that represents a group.
- [RCSHandle.Group](rcshandle/group.md)
  A structure that represents an RCS group handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcshandle/uri)*