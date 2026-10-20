# encode(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes the given value.

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
mutating func encode(_ value: Int32) throws
```

#### Discussion

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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(_:)-9d3m0)*