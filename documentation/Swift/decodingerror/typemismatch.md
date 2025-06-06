# DecodingError.typeMismatch(_:_:)

**Framework**: Swift  
**Kind**: case

An indication that a value of the given type could not be decoded because it did not match the type of what was found in the encoded payload.

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
case typeMismatch(any Any.Type, DecodingError.Context)
```

#### Discussion

As associated values, this case contains the attempted type and context for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/decodingerror/typemismatch(_:_:))*