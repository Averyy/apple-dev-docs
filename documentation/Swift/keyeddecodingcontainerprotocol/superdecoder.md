# superDecoder()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns a `Decoder` instance for decoding `super` from the container associated with the default `super` key.

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
func superDecoder() throws -> any Decoder
```

#### Return Value

A new `Decoder` to pass to `super.init(from:)`.

#### Discussion

Equivalent to calling `superDecoder(forKey:)` with `Key(stringValue: "super", intValue: 0)`.

> **Note**: `DecodingError.keyNotFound` if `self` does not have an entry for the default `super` key.

> **Note**: `DecodingError.valueNotFound` if `self` has a null entry for the default `super` key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/superdecoder())*