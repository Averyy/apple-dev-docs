# XMLParser.ExternalEntityResolvingPolicy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Defines the external entity resolving policy used by an `NSXMLParser` instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum ExternalEntityResolvingPolicy
```

```c
enum NSXMLParserExternalEntityResolvingPolicy : NSUInteger;
```

## Topics

### Constants
- [XMLParser.ExternalEntityResolvingPolicy.always](./externalentityresolvingpolicy-swift.enum/always.md)
  The parser always resolves external entities.
- [XMLParser.ExternalEntityResolvingPolicy.never](./externalentityresolvingpolicy-swift.enum/never.md)
  The parser should never resolve external entities.
- [XMLParser.ExternalEntityResolvingPolicy.noNetwork](./externalentityresolvingpolicy-swift.enum/nonetwork.md)
  The parser resolves external entities but does not load them over the network.
- [XMLParser.ExternalEntityResolvingPolicy.sameOriginOnly](./externalentityresolvingpolicy-swift.enum/sameoriginonly.md)
  The parser resolves external entities only from the same origin as the original URL. Only applies to `NSXMLParser` instances initialized with `-initWithContentsOfURL:`.
- [XMLParser.ExternalEntityResolvingPolicy.always](./externalentityresolvingpolicy-swift.enum/always.md)
  The parser always resolves external entities.
- [XMLParser.ExternalEntityResolvingPolicy.never](./externalentityresolvingpolicy-swift.enum/never.md)
  The parser should never resolve external entities.
- [XMLParser.ExternalEntityResolvingPolicy.noNetwork](./externalentityresolvingpolicy-swift.enum/nonetwork.md)
  The parser resolves external entities but does not load them over the network.
- [XMLParser.ExternalEntityResolvingPolicy.sameOriginOnly](./externalentityresolvingpolicy-swift.enum/sameoriginonly.md)
  The parser resolves external entities only from the same origin as the original URL. Only applies to `NSXMLParser` instances initialized with `-initWithContentsOfURL:`.
### Initializers
- [init?(rawValue: UInt)](./externalentityresolvingpolicy-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [class let errorDomain: String](./errordomain.md)
  Indicates an error in XML parsing.
- [XMLParser.ErrorCode](./errorcode.md)
  The following error codes are defined by `NSXMLParser`. For error codes not listed here, see the `<libxml/xmlerror.h>` header file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy-swift.enum)*