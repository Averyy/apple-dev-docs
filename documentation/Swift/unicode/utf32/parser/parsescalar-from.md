# parseScalar(from:)

**Framework**: Swift  
**Kind**: method

Parses a single Unicode scalar value from `input`.

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
mutating func parseScalar<I>(from input: inout I) -> Unicode.ParseResult<Unicode.UTF32.Parser.Encoding.EncodedScalar> where I : IteratorProtocol, I.Element == UInt32
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf32/parser/parsescalar(from:))*