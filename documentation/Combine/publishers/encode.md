# Publishers.Encode

**Framework**: Combine  
**Kind**: struct

A publisher that encodes elements received from an upstream publisher, using a given encoder.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Encode<Upstream, Coder> where Upstream : Publisher, Coder : TopLevelEncoder, Upstream.Output : Encodable
```

## Topics

### Creating a Encode Publisher
- [init(upstream: Upstream, encoder: Coder)](publishers/encode/init(upstream:encoder:).md)
  Creates a publisher that decodes elements received from an upstream publisher, using a given decoder.
### Declaring Publisher Topography
- [Publishers.Encode.Output](publishers/encode/output.md)
  The kind of values published by this publisher.
- [Publishers.Encode.Failure](publishers/encode/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/encode/upstream.md)
### Applying Operators
- [Publisher Operators](publishers-encode-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/encode/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Decode](publishers/decode.md)
  A publisher that decodes elements received from an upstream publisher, using a given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/encode)*