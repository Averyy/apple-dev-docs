# encodeConditional(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).

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
mutating func encodeConditional<T>(_ object: T) throws where T : AnyObject, T : Encodable
```

#### Discussion

For encoders which don’t support this feature, the default implementation encodes the given object unconditionally.

For formats which don’t support this feature, the default implementation encodes the given object unconditionally.

> **Note**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

`EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Parameters

- `object`: The object to encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encodeconditional(_:))*