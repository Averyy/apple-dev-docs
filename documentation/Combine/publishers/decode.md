# Publishers.Decode

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that decodes elements received from an upstream publisher, using a given decoder.

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
struct Decode<Upstream, Output, Coder> where Upstream : Publisher, Output : Decodable, Coder : TopLevelDecoder, Upstream.Output == Coder.Input
```

## Topics

### Creating a decode publisher
- [init(upstream: Upstream, decoder: Coder)](./decode/init%28upstream,decoder%29.md)
  Creates a publisher that decodes elements received from an upstream publisher, using a given decoder.
### Declaring supporting types
- [Publishers.Output](./output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.Decode.Failure](./decode/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./decode/upstream.md)

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Encoding and decoding
- [Publishers.Encode](./encode.md)
  A publisher that encodes elements received from an upstream publisher, using a given encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/decode)*