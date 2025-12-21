# TopLevelDecoder

**Framework**: Combine  
**Kind**: protocol

A type that defines methods for decoding.

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
protocol TopLevelDecoder
```

## Topics

### Declaring supporting types
- [associatedtype Input](topleveldecoder/input.md)
  The type this decoder accepts.
### Decoding
- [func decode<T>(T.Type, from: Self.Input) throws -> T](topleveldecoder/decode(_:from:).md)
  Decodes an instance of the indicated type.

## See Also

- [protocol TopLevelEncoder](toplevelencoder.md)
  A type that defines methods for encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/topleveldecoder)*