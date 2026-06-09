# XMLParser.ExternalEntityResolvingPolicy.never

**Framework**: Foundation  
**Kind**: case

The parser should never resolve external entities.

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
case never
```

## See Also

- [XMLParser.ExternalEntityResolvingPolicy.always](xmlparser/externalentityresolvingpolicy-swift.enum/always.md)
  The parser always resolves external entities.
- [XMLParser.ExternalEntityResolvingPolicy.noNetwork](xmlparser/externalentityresolvingpolicy-swift.enum/nonetwork.md)
  The parser resolves external entities but does not load them over the network.
- [XMLParser.ExternalEntityResolvingPolicy.sameOriginOnly](xmlparser/externalentityresolvingpolicy-swift.enum/sameoriginonly.md)
  The parser resolves external entities only from the same origin as the original URL. Only applies to `NSXMLParser` instances initialized with `-initWithContentsOfURL:`.
- [XMLParser.ExternalEntityResolvingPolicy.always](xmlparser/externalentityresolvingpolicy-swift.enum/always.md)
  The parser always resolves external entities.
- [XMLParser.ExternalEntityResolvingPolicy.noNetwork](xmlparser/externalentityresolvingpolicy-swift.enum/nonetwork.md)
  The parser resolves external entities but does not load them over the network.
- [XMLParser.ExternalEntityResolvingPolicy.sameOriginOnly](xmlparser/externalentityresolvingpolicy-swift.enum/sameoriginonly.md)
  The parser resolves external entities only from the same origin as the original URL. Only applies to `NSXMLParser` instances initialized with `-initWithContentsOfURL:`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy-swift.enum/never)*