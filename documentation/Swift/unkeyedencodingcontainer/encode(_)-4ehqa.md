# encode(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes the given value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func encode(_ value: UInt128) throws
```

## Discussion

> **Throws**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Parameters

- `value`: The value to encode.

## Default Implementations

### UnkeyedEncodingContainer Implementations
- [func encode(UInt128) throws](./encode%28_%29-7suq1.md)
  Encodes the given value.
- [func encode(Int128) throws](./encode%28_%29-8m4kj.md)
  Encodes the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(_:)-4ehqa)*