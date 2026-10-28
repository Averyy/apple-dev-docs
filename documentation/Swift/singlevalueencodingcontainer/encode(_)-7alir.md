# encode(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a single value of the given type.

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
mutating func encode(_ value: Int128) throws
```

## Discussion

> **Throws**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

> **Precondition**: May not be called after a previous `self.encode(_:)` call.

## Parameters

- `value`: The value to encode.

## Default Implementations

### SingleValueEncodingContainer Implementations
- [func encode(Int128) throws](./encode%28_%29-5lw48.md)
  Encodes a single value of the given type.
- [func encode(UInt128) throws](./encode%28_%29-6x0pw.md)
  Encodes a single value of the given type.
- [func encode(Int128) throws](./encode%28_%29-82sdy.md)
  Encodes a single value of the given type.
- [func encode(UInt128) throws](./encode%28_%29-wjsd.md)
  Encodes a single value of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevalueencodingcontainer/encode(_:)-7alir)*