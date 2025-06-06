# encode(_:)

**Framework**: Swift  
**Kind**: method  
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
mutating func encode(_ value: UInt128) throws
```

#### Discussion

> **Note**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

`EncodingError.invalidValue` if the given value is invalid in the current context for this format.

> **Note**: May not be called after a previous `self.encode(_:)` call.

May not be called after a previous `self.encode(_:)` call.

## Parameters

- `value`: The value to encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevalueencodingcontainer/encode(_:)-5kf5u)*