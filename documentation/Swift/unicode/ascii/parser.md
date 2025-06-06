# Unicode.ASCII.Parser

**Framework**: Swift  
**Kind**: struct

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Parser
```

## Topics

### Initializers
- [init()](unicode/ascii/parser/init.md)
  Constructs an instance that can be used to begin parsing `CodeUnit`s at any Unicode scalar boundary.
### Instance Methods
- [func parseScalar<I>(from: inout I) -> Unicode.ParseResult<Unicode.ASCII.Parser.Encoding.EncodedScalar>](unicode/ascii/parser/parsescalar(from:).md)
  Parses a single Unicode scalar value from `input`.
### Type Aliases
- [Unicode.ASCII.Parser.Encoding](unicode/ascii/parser/encoding.md)
  The encoding with which this parser is associated

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/ascii/parser)*