# DecodingError.keyNotFound(_:_:)

**Framework**: Swift  
**Kind**: case

An indication that a keyed decoding container was asked for an entry for the given key, but did not contain one.

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
case keyNotFound(any CodingKey, DecodingError.Context)
```

#### Discussion

As associated values, this case contains the attempted key and context for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/decodingerror/keynotfound(_:_:))*